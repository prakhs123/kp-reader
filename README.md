# kp-reader
Better version of kp-reader books, contains texts converted through openai. More readable, comprehensible.
Using pandoc to convert all markdowns to epub

`pandoc --from markdown --to epub -s -V block-headings --toc --no-highlight --css github-markdown.min.css --output kp-reader-2.epub title.txt kp-reader-2.md`
`pandoc --from markdown --to epub -s -V block-headings --toc --no-highlight --css github-markdown.min.css --output kp-reader-3-theoretical.epub title.txt kp-reader-3-theoretical.md`
`pandoc --from markdown --to epub -s -V block-headings --toc --no-highlight --css github-markdown.min.css --output kp-reader-3-practical.epub title.txt kp-reader-3-practical.md`