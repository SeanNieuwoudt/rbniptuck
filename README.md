# Nip n Tuck

A simple script to recursively scan Ruby projects and convert all old style hashes ( => ) to the newer Ruby 1.9^ compliant hash syntax.

From this:

    hash {
      :key => "Value"
    }

To this:

    hash {
      key: 'Value'
    }

While we're at, double quoted Ruby strings get converted to their single quoted equivalent.

From this:

    "This string"

To this:

    'This string'

The script will ignore double quoted strings that are being interpolated.

### How to use it

    $> python niptuck.py
    $> python niptuck.py --dir . --ext rb

##### Options are:

* `--dir` or `-d` to specify the directory
* `--ext` or `-e` to specify the file extensions to look for
* `--cnt` or `-c` to make the script only count occurrences and not do the replacement

## Examples

To get a count of how many occurrences will be replaced:

    $> python niptuck.py -d . -c y

To go ahead and replace the occurrences in the `app` directory:

    $> python niptuck.py -d ./app
