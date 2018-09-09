from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def main():
    print('Starting...')
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    drive_service = build('drive', 'v3', http=creds.authorize(Http()))
    print('Authorized!')

    page_token = None
    searchTerms = ['Chemistry 10H Notes' , 'AP World Notes']
    searchTermNewParentID = ['1uMfiMCEBV5MZbFf4kB0IBm4U95E49u29' , '1XvHDFGfF-Vd-NV-um_qfSlN-aYEjjW5X']
    for i in range (0, len(searchTerms)):
        print('On loop #' + str(i))

        searchStringArray = []
        searchStringArray.append("name contains '")
        searchStringArray.append(searchTerms[i])
        searchStringArray.append("'")

        searchString = ''.join(searchStringArray)

        print(searchString)
        while True:
            response = drive_service.files().list(q = searchString).execute()
            print('Finished searching for ' + searchTerms[i])
            for changeFile in response.get('files', []):
                print ('Found file: ' , changeFile.get('name') , changeFile.get('id'))
                # Process change
                file_id = changeFile.get('id')
                # Retrieve the existing parents to remove
                changeFile = drive_service.files().get(fileId=file_id,
                                                 fields='parents').execute()
                previous_parents = ",".join(changeFile.get('parents'))
                # Move the changeFile to the new folder
                changeFile = drive_service.files().update(fileId=file_id,
                                                    addParents=searchTermNewParentID[i],
                                                    removeParents=previous_parents,
                                                    fields='id, parents').execute()
                print ('Moved file: %s (%s)' % (changeFile.get('name') , changeFile.get('id)')))
            print('Finished Moving!')    
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

if __name__ == '__main__':
    main()