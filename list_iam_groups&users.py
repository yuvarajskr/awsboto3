import boto3

def extract_values(obj, key):
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

client = boto3.client('iam')

response = client.list_groups(MaxItems=123)
val = extract_values(response,'GroupName')
print("Available Groups" , val)

response = client.list_users(MaxItems=123)
val = extract_values(response,'UserName')
print("Availale Users ", val)

