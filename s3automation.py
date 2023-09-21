import boto3
while True:
    print("Menu")
    print("1. For Create S3 bucket")
    print("2. For Display All bucket")
    print("3. For display Bucket content")
    print("4. For Upload content")
    print("5. For Delete content")
    print("6. For Delete Bucket")
    print("7. For Quit")
    op=int(input("Select Any Option"))
    if op==1:
        regname=input("Enter The Region Name")
        bname=input("Enter The bucket name")
        s3_client = boto3.client('s3', region_name=regname)
        location = {'LocationConstraint': regname}
        s3_client.create_bucket(Bucket=bname,CreateBucketConfiguration=location)
        print("Bucket Create successfully")
    elif op==2:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    elif op==3:
        bname=input("Enter Bucket Name")
        from boto3 import client
        conn = client('s3')
        for key in conn.list_objects(Bucket=bname)['Contents']:
            print(key['Key'])
    elif op==4:
        bname=input("Enter The Existing bucket Name")
        fname=input("Enter the file full path")
        s3 = boto3.client('s3')
        with open(fname, "rb") as f:
            s3.upload_fileobj(f, bname, fname)
        print("File Upload Successfully")
    elif op==5:
        bname=input("Enter The Existing bucket Name")
        fname=input("Enter the file  Name")
        import boto3
        s3 = boto3.resource('s3')
        s3.Object(bname, fname).delete()
        print("Data Deleted Success Fully")
    elif op==6:
        bname=input("Enter The Existing bucket Name")
        import boto3
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bname)
        bucket.delete()
        print("Bucket Deleted SuccessFully")
    elif op==7:
        exit()
    else:
        print("Invalid Option Please select correct Option")
