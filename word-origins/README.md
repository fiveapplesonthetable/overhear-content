# Editorial source review

The reviewed collection contains 22 Russian and 22 French histories. The target is a sourced Origin entry for every served dictionary word; [COVERAGE.md](COVERAGE.md) records the current gaps. Start with the most frequent words in published audio, then new episode vocabulary. This includes grammar words, names and phrases. A genuinely unknown or disputed origin is an acceptable reviewed conclusion when the uncertainty and its supporting source are explicit. French histories were checked against individual entries in the ninth edition of the Dictionnaire de l’Académie française. Russian histories were checked against scanned pages of M. Vasmer’s dictionary hosted by the Vinogradov Institute of the Russian Academy of Sciences. Every entry links its particular source; the institute viewer may require a DjVu reader.

Do not attach a generic dictionary home page to an unchecked claim. Recovered legacy histories remain in the previous content-branch commit and the local review archive; they are not approved by recovery alone. Add them as they are checked, with a specific supporting entry. Distinguish historical word formation from modern morpheme analysis and from mnemonic similarities. Keep competing or uncertain origins qualified.

This metadata is independent of scene render hashes. Expanding or correcting the checked set does not require new audio or another APK once the Origin screen is installed.

`tools/origin_coverage.py` inventories only the dictionary shards named by a verified serving catalogue and checks their digests. It reports coverage and a complete missing-word queue without treating a link as proof of a claim. Regenerate the report whenever the served dictionary grows.
