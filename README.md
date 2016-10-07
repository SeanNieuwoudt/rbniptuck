# Nip n Tuck

A simple script to recursively scan Ruby projects and convert all old style hashes to the newer Ruby 1.9^ compliant hash syntax.

From this:

    hash { 
      :key => "Value"
    }
    
To this: 

    hash { 
      key: 'Value'
    }
    
While we're at, uninterpolated double quoted Ruby strings get converted to their single quoted equivalent. 

From this: 

    "This string"
    
To this: 

    'This string'
    

### How to use it

    $> python niptuck.py --dir ./src --ext .rb
    
    
##### Options are:

* `--dir` or `-d` to specify the directory
* `--ext` or `-e` to specify the file extensions to look for
* `--cnt` or `-c` to make the script only count occurrences and not do the replacement

## Examples

If you want to check how many occurrences of the old style Ruby hash are in your legacy Rails codebase:

    $> python niptuck.py -d ./app -c y
    
If you want to go ahead and replace all occurrences of the old style Ruby hashes and double quoted strings:

    $> python niptuck.py -d ./app 

