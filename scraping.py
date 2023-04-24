## Code to download tutorials from TutorialsPoint.com
import urllib.request
import sys

def report(blocknr, blocksize, size):
    current = blocknr*blocksize
    sys.stdout.write("\r{0:.2f}%".format(100.0*current/size))
    sys.stdout.flush()

def downloadFile(url):
    fname = url.split('/')[-1]
    urllib.request.urlretrieve(url, fname, reporthook=report)
    print ("Download starting...")

tld = "https://www.tutorialspoint.com/"
# enter the name of the tutorial
print ("Name of Tutorial? ")
query = input().lower()
url = tld + query + '/' + query + '_tutorial.pdf'
downloadFile(url)
print ("\nComplete PDF for " + query.capitalize() + " has been downloaded.\n")
