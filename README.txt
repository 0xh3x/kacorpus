Scripts for building Georgian text corpus from internet.

#TODO howto

wget "http://dumps.wikimedia.org/kawiki/latest/kawiki-latest-pages-meta-current.xml.bz2"
bunzip2 kawiki-latest-pages-meta-current.xml.bz2
python wikidump2text.py kawiki-latest-pages-meta-current.xml wikitext.txt

