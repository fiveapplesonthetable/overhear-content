#!/bin/bash
# Narrator method B, one episode per invocation, so each episode can be published as soon as its run ends.
#
#   narrator_batch.sh kukhnya-s01e01 kukhnya-s01e02 ... [-- extra pipeline.py args, e.g. --retry-failed]
#
# Each episode is its own `pipeline.py --narrator-only --episode E` run (it takes pipeline.lock, the GPU goes through gpurun, scene commits take
# publish.lock). The script prints "EPISODE-DONE <id> status=<n>" after each one; an episode that exits 0 is ready to publish
# (publish/run-scheduled.sh or publish/publish.py --all --verify). A failed episode does not stop the rest; the exit status is the number of failures.
# Failed lines are remembered per render key (narrator-failures.jsonl, failed.json): re-running an episode only does what is missing.
# OVERHEAR_CONTENT must be set explicitly to the content checkout the scenes were rendered from (e.g. a content checkout); the narrator
# refuses scenes whose contentHash it does not match. A pipeline.lock that stays busy for 6 h ends the wait for that episode (counted as failed).
set -u
[ -n "${OVERHEAR_CONTENT:-}" ] || { echo "set OVERHEAR_CONTENT to the content checkout the scenes were rendered from" >&2; exit 2; }
[ -d "$OVERHEAR_CONTENT/out" ] || { echo "OVERHEAR_CONTENT=$OVERHEAR_CONTENT has no out/ directory" >&2; exit 2; }
export OVERHEAR_CONTENT
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
eps=()
while [ $# -gt 0 ] && [ "$1" != "--" ]; do eps+=("$1"); shift; done
[ "${1:-}" = "--" ] && shift
[ ${#eps[@]} -gt 0 ] || { echo "usage: $0 EPISODE [EPISODE ...] [-- pipeline.py args]" >&2; exit 2; }
bad=0
for ep in "${eps[@]}"; do
  echo "=== $(date -u +%FT%TZ) narrator $ep"
  # 75: another pipeline run holds pipeline.lock (the renderer works scene by scene); wait for it rather than skip the episode.
  waited=0
  while :; do
    nice -n 19 ${OVERHEAR_CPUSET:+taskset -c "$OVERHEAR_CPUSET"} python3 "$here/pipeline.py" --narrator-only --episode "$ep" "$@"
    st=$?
    [ $st -eq 75 ] || break
    [ $waited -eq 0 ] && echo "pipeline.lock is busy; waiting for it (up to 6 h)"
    [ $waited -ge 21600 ] && { echo "pipeline.lock still busy after 6 h; giving up on $ep"; break; }
    sleep 30
    waited=$((waited + 30))
  done
  echo "EPISODE-DONE $ep status=$st at $(date -u +%FT%TZ)"
  [ $st -eq 0 ] || bad=$((bad + 1))
done
exit $bad
