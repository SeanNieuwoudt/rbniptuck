# Nip n Tuck

A simple script to recursively scan Ruby projects and convert all old style hashes to the newer Ruby 1.9^ compatible structure. 

From this:

    hash { 
      :key => "Value"
    }
    
To this: 

    hash { 
      key: 'Value'
    }
    
While we're at, un-interpolated double quoted Ruby strings get converted to their single quoted equivalent. 

From this: 

    "This string"
    
To this: 

    'This string'
    

### How to use it

    $> python niptuck.py --dir ./src --ext .rb
    

