import boto3

aws_manag_cons = boto3.session.Session(profile_name="root")
s3_cons = aws_manag_cons.resource('s3')

for each_bucket in s3_cons.buckets.all():
    print (each_bucket)