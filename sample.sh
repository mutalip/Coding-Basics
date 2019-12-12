  #!/bin/bash

         a=$(cat input| head -n 1 | awk '{print $1}')
         b=$(cat input| head -n 1 | awk '{print $2}')
         echo $((a+b))
