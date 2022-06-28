import re

# difining Different data types
types={'integer' : "<class 'int'>",
        'string' : "<class 'str'>", 
        'boolean' : "<class 'bool'>", 
        'list' : "<class 'bool'>",
        'dictionary': "<class 'dict'>",
        'tuple': "<class 'tuple'>",
        }

errors={}

def validator(dict={}, validation_rules={}):
    global types, errors
    for var in validation_rules:
        err={}
        for v in validation_rules[var]:
            if (((v == 'type') and (str(type(dict[var])) != types[validation_rules[var][v]]))):
                err[v] = "Type doesn't matched (Validation: {}, obtained: {})".format(types[validation_rules[var][v]], type(dict[var]))

            elif(v == 'minLength' and (len(dict[var]) < validation_rules[var][v])):
                err[v] = "Length less than minimum (minimum Length: {}, obtained length: {})".format(validation_rules[var][v], len(dict[var]))

            elif(v == 'maxLength' and (len(dict[var]) > validation_rules[var][v])):
                err[v] = "Length exceed than maximum (maximum Length: {}, obtained length: {})".format(validation_rules[var][v], len(dict[var]))

            elif(v == 'required' and ((validation_rules[var][v] == True) and not(dict[var]))):
                err[v] = "Required Field is set to {} for {}.".format(validation_rules[var][v], v)
                  
            elif (v == 'minValue' and (dict[var] < validation_rules[var][v])):
                err[v] = "Minimum Value error (minimum value: {}, obtained value: {})".format(validation_rules[var][v], dict[var])

            elif(v == 'maxValue' and (dict[var] > validation_rules[var][v])):
                err[v] = "Maximum value error (Maximum value: {}, obtained value: {})".format(validation_rules[var][v], dict[var])

            elif(v == 'regex' and (not re.fullmatch(re.compile(validation_rules[var][v]), dict[var]))):
                err[v] = "Regex matching error occurs (Set patterns: {} obtained value: {})".format(validation_rules[var][v], dict[var])

            elif(v == 'enumerate' and (dict[var] not in validation_rules[var][v])):
                err[v] = "Out of defined value (Set values: {}, obtained value: {})".format(validation_rules[var][v], dict[var])

        if(err):
            errors[var]=err
    
    if(errors): # If any Error
        return False
    else:
        return True



validation_rules={
    'name':{
        'type': 'string',
        'minLength':10,
        'maxLength': 500
    },
    'address':{
        'type': 'string',
        'minLength': 10,
        'maxLength':50,
        'required':True,
    },
    'age':{
        'type': 'integer',
        'minValue': 5,
        'maxValue':30,
    },
    'email':{
        "regex" : "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
    },
    'day':{
        'enumerate':['sunday', 'monday', 'tuesday', 'thrusday', 'friday', 'saturday']
    },
    'birthYear':{
        'maxValue':2022,
    }
}


dict ={'name': 'Bhuban Yadav', 'age':24, 'day':'monday' ,'birthYear':2023, 'birthMonth': 4, 'birthDay': 18, 'address': 'Dhapakhel-23, Lalitpur Nepal','email':'yadav.bhuban.by@gmail.com'}




print(validator(dict, validation_rules))
print(errors if(errors) else "")
