# Google Drive Note Sorter
Used to sort notes into folders based on name.
# How to Use
1. Turn on Drive API and install the library here: https://developers.google.com/drive/api/v3/quickstart/python
2. Place the credentials.json from the API activation and place it in the same folder as NoteSorter.py
3. Edit NoteSorter.py and change the search terms array to match the file name to search for (searches for any file name that contains the string in searchTerms)
4. Change the searchTermNewParentID strings to the corresponding destination folder. You can find the folder id at the end of the URL of the destination folder. Navigate to the destination folder in Google Drive, and copy the string after "folders/".
5. Run NoteSorter.py and allow the program access to your Drive