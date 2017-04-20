secs=$(date +%s --date="$1")
date '+%d.%b.%Y %T' --date="@$((secs + 3662))"
