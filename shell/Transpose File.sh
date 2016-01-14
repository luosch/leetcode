# Read from the file file.txt and print its transposed content to stdout.
awk '
    {
        for (i=1; i<=NF; i++)
        {   
            if (line[i] == )
            {
                line[i] = 
            }
            else
            {
                line[i] = line[i] 
            }
        }
    }
    END {
        for (i=1; i<=NF; i++)
        {
            print line[i]
        }
    }
    ' file.txt
