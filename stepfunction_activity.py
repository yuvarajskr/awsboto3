import boto3
import json
client = boto3.client('stepfunctions',region_name='ap-south-1')

def json_values(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

print("Ready to start...")
response = client.list_activities(maxResults=123)

ativity_name = json_values(response,'name')
activity_arn = json_values(response,'activityArn')
print("Availale User : {} Arn: {}", ativity_name[0],activity_arn[0])

response = client.get_activity_task(activityArn = activity_arn[0])
print(response)
inputs = json_values(response,'input')
task_token = json_values(response,'taskToken')
tasktoken = task_token[0]
print("Task Token",task_token )
print(inputs[0])
inputs = json.loads(inputs[0])
values = []
for i in inputs : 
    values.append(inputs[i]+'')
fname = ""
for value in values:
    fname += ' '+value
opt = fname[1:]
opt = ('"'+opt+'"')
response = client.send_task_success(taskToken= tasktoken,output= opt )
print(response)


