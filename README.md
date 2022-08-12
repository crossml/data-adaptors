# Input Adaptor pipeline for uploading documents on the cloud.

What you can expect from this repository:

- Efficient ways to get documents uploaded on the cloud.

## Quick Tour

Upload documents on the cloud in an easy way.

## installation

Developer mode

```
git clone 'repo link'
```

User mode

```
pip install data-adaptor
```

## Getting start

```
from DataAdaptor import InputAdaptor
adaptor=InputAdaptor()
```

```
# path of the file
file=''

# name of cloud
cloud_name=''

# upload file on cloud
adaptor.file_upload(file,cloud_name)

# upload zip file on cloud
adaptor.zip_upload(file,cloud_name)

# upload file on the cloud through URL
adaptor.url_upload(url,cloud_name)

# upload FTP folder files on cloud
adaptor.ftp_upload(ftp_host, username, password, ftp_folder_path,cloud_name)
```

# Documentation:

The full package documentation is available here.

First of all, you have to install the data-adaptor package.
then create an object of InputAdaptor

```
from DataAdaptor import InputAdaptor
adaptor=InputAdaptor()
```

## File upload on the cloud:

To upload the tif, png, jpg, jpeg, or pdf file on the cloud user have to call the file_upload method of InputAdaptor and pass the file path and cloud name where the user wants to store the file on the cloud.

```
adaptor.file_upload(file, cloud_name)
```

## Zip upload:

To upload the zip file user have to call the zip_upload method of InputAdaptor and pass the file path and cloud name where the user wants to store the zip file on the cloud.

Note: Zip files contain only valid extension files like jpg, jpeg, tif, png, and pdf.

```
adaptor.zip_upload(path, cloud_name)
```

## Url Upload:

To upload the file to the cloud with the help of an online URL user have to call the url_upload method of Input_Adaptor and pass the URL and cloud name as the parameters in a method where the user wants to store the file on the cloud.

```
adaptor.url_upload(url, cloud_name)
```

## FTP file upload:

To upload a file from FTP to the cloud user have to call the ftp_upload method of InputAdaptor and pass the parameters FTP hostname, username, password, FTP folder path, and cloud name where the user wants to store the files on the cloud.

```
adaptor.ftp_upload(ftp_host, username, password, ftp_folder_path,cloud_name)
```