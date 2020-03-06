#!/usr/bin/env python3


from ansible.module_utils.basic import *

def main():
    fields = {"var1": {"required": True, "type": "str"}, "var2": {"required": True, "type": "str"}} 
    module = AnsibleModule(argument_spec=fields)
    var1= module.params['var1']
    var2= module.params['var2']
    response = {var1: var2}
    print("TEST LECTURE SCRIPT")
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
