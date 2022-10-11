import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = "https://s3.ap.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "oJ6E6t5-rl6eIVRQ4eeVBdfjzoqeArtZ1ZwlcJjXaJ3a" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/2015e0c2422945669af3d7c6bf72213a:e588c70c-1844-49c9-9468-ed3f240e0d03::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

# {
#   "apikey": "oJ6E6t5-rl6eIVRQ4eeVBdfjzoqeArtZ1ZwlcJjXaJ3a",
#   "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
#   "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloud-object-storage:global:a/2015e0c2422945669af3d7c6bf72213a:e588c70c-1844-49c9-9468-ed3f240e0d03:resource-key:5afc8e5b-b54f-40f5-810b-24b4ee0af992",
#   "iam_apikey_name": "Service credentials-1",
#   "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Reader",
#   "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/2015e0c2422945669af3d7c6bf72213a::serviceid:ServiceId-33c1d3f9-2ad3-472c-a648-c3919ba62db4",
#   "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/2015e0c2422945669af3d7c6bf72213a:e588c70c-1844-49c9-9468-ed3f240e0d03::"
# }

# Create client 
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)


def get_buckets():
    print("Retrieving list of buckets")
    try:
        buckets = cos.buckets.all()
        for bucket in buckets:
            print("Bucket Name: {0}\n".format(bucket.name))
            get_bucket_contents(bucket.name)
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))

def get_bucket_contents(bucket_name):
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:
        files = cos.Bucket(bucket_name).objects.all()
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))

def create_bucket(bucket_name):
    print("Creating new bucket: {0}".format(bucket_name))
    try:
        cos.Bucket(bucket_name).create(
            CreateBucketConfiguration={
                "LocationConstraint":"ap-geo"
            }
        )
        print("Bucket: {0} created!".format(bucket_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to create bucket: {0}".format(e))

# create_bucket("my_bucket")
get_buckets()

