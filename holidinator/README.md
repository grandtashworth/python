Holidinator - The Holiday Determinator
--------------------------------------
The holidinator consists of two scripts for cgi-bin

1. a cgi-bin bash parser script called h (nice and small for calling by adding to other scripts)
2. a python3 script called qdate which needs QuantLib in either the venv or base install you are using

How to Run
----------

Make sure you have a webserver running, with cgi-bin enabled to run scripts (you may need to enable booleans if you are enforcing and change capabilities (setcap) on executables or create AVC exceptions) and the h script is executable (0555 should be enough) Then copy the (qdate) script to the cgi-bin directory along with the h bash script.

The way I run this script is from another script to answer the age old question of whether "today" is a holiday. As humans that's easy, but machines need a little more coaxing, especially if it is a monolithic monitoring system, or a production system that doesnt need to start up it's software on a public holiday. All you need to add to your script is something like the function below where the $_calval needs to be determined by whatever makes sense to you (some people call their hostnames after geographical locations, other people use a cmdb and generate facts) the $_calval is a calendar location such as Australia, UnitedKingdom, UnitedStates (see QuantLib docs on this)

Example:
```javascript
#!/bin/bash
__today(){
        _calval=$1
        [[ -z $_calval ]] && {
		# assume you are living in the UK
                _calval=UnitedKingdom
	}
        _holiday=$(curl -G -d cal=${_calval} -d day=$(date +%d) -d month=$(date +%m) -d year=$(date +%Y) http://olympus/cgi-bin/h 2>/dev/null)
        case $_holiday in
                True)
                echo "Today is a holiday, nothing to see here..."
                exit 0
                ;;
                False)
                ;;
                *)
                ;;
        esac
}
__today UnitedStates
__today Australia
exit $?
```
