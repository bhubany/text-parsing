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
            if (v == 'type'):
                if(f"{type(dict[var])}" != types[validation_rules[var][v]]):
                    err[v] = "Type Doesnot Matched (Validation: {}, obtained: {})".format(types[validation_rules[var][v]], type(dict[var]))

            elif(v == 'minLength'):
                if(len(dict[var]) < validation_rules[var][v]):
                    err[v] = "Length less than minimum (minimum Length: {}, obtained length: {})".format(validation_rules[var][v], len(dict[var]))

            elif(v == 'maxLength'):
                if(len(dict[var]) > validation_rules[var][v]):
                    err[v] = "Length exceed than maximum (maximum Length: {}, obtained length: {})".format(validation_rules[var][v], len(dict[var]))

            elif(v == 'required'):
                if((validation_rules[var][v] == True) and not(dict[var])):
                    err[v] = "Required Field is set to {} for {}.".format(validation_rules[var][v], v)
                  
            elif (v == 'minValue'):
                if(dict[var] < validation_rules[var][v]):
                    err[v] = "Minimum Value error (minimum value: {}, obtained value: {})".format(validation_rules[var][v], dict[var])

            elif(v == 'maxValue'):
                if(dict[var] > validation_rules[var][v]):
                    err[v] = "Maximum value error (Maximum Length: {}, obtained length: {})".format(validation_rules[var][v], dict[var])

            elif(v == 'regex'):
                patterns = re.compile(validation_rules[var][v], re.I)
                if(not re.fullmatch(patterns, dict[var])):
                    err[v] = "Regex matching error occurs (Set patterns: {} obtained value: {})".format(validation_rules[var][v], dict[var])

            elif(v == 'enumerate'):
                if(dict[var] not in validation_rules[var][v]):
                    err[v] = "Out of defined value (Set values: {}, obtained value: {})".format(validation_rules[var][v], dict[var])

            else:
                print("Validator not Found ")
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
        'type': 'integer',
        'minLength': 100,
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
    }
}


dict ={'name': 'Bhuban Yadav', 'age':24, 'day':'noday' ,'birthYear':1998, 'birthMonth': 4, 'birthDay': 18, 'address': 'Dhapakhel-23, Lalitpur Nepal','email':'yadav.bhuban.by@gmail.com'}




print(validator(dict, validation_rules))
print("Errors: {}".format(errors))
