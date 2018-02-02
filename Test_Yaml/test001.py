coding = "UTF-8"
import yaml
#
# with open("./data.yaml","r") as f:
#     data = yaml.load(f)
    # print(data)
    # Test_data = data.get("Test")
    # print(Test_data)
    # for i in Test_data.keys():
    #     print("test: %s \ntest_name: %s \ntest_pwd: %s \n" %
    #           (i,Test_data.get(i).get("name"),Test_data.get(i).get("pwd")))


with open("./data.yaml","r") as f:
    data = yaml.load(f)
    data.get("Test").pop("code")
    print(data)
