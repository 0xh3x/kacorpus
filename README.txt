Scripts for building Georgian text corpus from internet.


sudo apt-get install python-scrapy antiword

#TODO howto
cd wiki/
wget "http://dumps.wikimedia.org/kawiki/latest/kawiki-latest-pages-meta-current.xml.bz2"
bunzip2 kawiki-latest-pages-meta-current.xml.bz2
python wikidump2text.py kawiki-latest-pages-meta-current.xml ../wikitext.txt

cd ../bukige
scrapy crawl buki.ge
antiword *.doc>../bukigetext.txt
rm *.doc

cd ../libge
scrapy crawl lib.ge


cd ../nplggovge
scrapy crawl nplg.gov.ge
find . -name '*.pdf' -exec pdftotext {} \;

