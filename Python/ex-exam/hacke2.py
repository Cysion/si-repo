"""
Om man kör funktionen remove_comments() från förra uppgiften kan den krascha, 
om filen man ska läsa inte finns. Visa hur man kan använda undantagshantering 
(exception) för att förhindra att programmet kraschar i det fallet.
"""

def remove_comments(in_filename, out_filename):
    in_handle = open(in_filename, 'r')
    out_handle = open(out_filename, 'w')
    for line in in_handle:
        out_handle.write(clean_line(line))