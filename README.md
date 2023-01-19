# kp-reader
Better version of kp-reader books, contains texts converted through openai. More readable, comprehensible.

KP-Reader-2

Using pandoc to convert all markdowns to epub

`pandoc -o kp-reader-2.epub title.txt 1-LETTERS\ TO\ THE\ AUTHOR.md 2-AN\ INTERVIEW\ WITH\ THE\ AUTHOR.md 3-ASTROLOGY\ -\ AN\ OCCULT\ SCIENCE.md 4-HISTORY\ OF\ ASTROLOGY.md 5-NADIS.md 6-Astrology-available\ data\ incomplete.md 7-Qualifications\ of\ an\ astrologer.md 8-ADVICE\ TO\ ADMINISTRATOR.md 9-Astrology-its\ use\ and\ limitations.md 10-KARMA\ -\ INEQUALITY\ IN\ LIFE.md 11-DESTINY\ FATE\ INEVITABLE.md 12-Shanti\ to\ ward\ off\ evil.md 13-BRANCHES\ OF\ ASTROLOGY.md 14-WHO\ CAN\ LEARN\ ASTROLOGY.md 15-TWELVE\ SIGNS\ OF\ THE\ ZODIAC.md 16-WHAT\ THE\ TWELVE\ SIGNS\ SIGNIFY.md 17-THE\ TWELVE\ HOUSES\ AND\ THEIR\ SIGNIFICANCE.md 18-1-SUN\ THE\ FATHER.md 18-2-Moon-The\ Mother.md 18-3-MARS-THE\ BROTHER.md 18-4-MERCURY-THE\ UNCLE.md 18-5-JUPITER-THE\ CHILDREN.md 18-6-VENUS\ -\ THE\ PLEASANT\ PARTNER.md 18-7-SATURN\ -\ SANI.md 18-8-THE\ NODES\ -\ RAHU\ AND\ KETHU.md 18-9-URANUS\ \(HERSCHEL\).md 18-10-NEPTUNE.md 18-11-FORTUNA.md`

`pandoc --from markdown --to epub3 --toc --no-highlight --output kp-reader-2.epub title.txt kp-reader-2.md`

Using ebook-convert from Calibre for standardising

`ebook-convert kp-reader-2.epub kp-reader-2-converted.epub`