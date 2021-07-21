import java.util.Scanner;
import java.io.PrintStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
public class Form {
    public static void main(String[] args) throws FileNotFoundException {
        PrintStream output = new PrintStream(new FileOutputStream("./tmp.html"));
        System.setOut(output);
        Scanner scan = new Scanner(System.in);
        
        System.err.println("input title:");
        String title = scan.nextLine();
        System.err.println("input text:");
        String text = scan.nextLine();
        System.err.println("input picture name:");
        String piclink = scan.nextLine();

        final String HEAD = 
        """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="../css/article.css">
            <script type="text/javascript" src="../js/setHead.js"></script>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
            <title>""" + title + 
        """
        </title>
        </head>
        <body>
            <iframe id="head"></iframe><script>setHead()</script>
			
            <div>
                    <h1>""" + title + 
        """
        </h1>
            </div>
        """;
        
        String REAR =
        """
        </body>
        </html>
        """;
        
        final String DIVS =
        """
        <div>
        """;
        
        final String DIVE =
        """
            
        </div>
        """;
        
        final String PS = "<p>" , PE = "</p>";
                        
        
        String IMG = "<img class=\"txtpic\" src=\"../pic/" + piclink + "\" />";
        
        String para = DIVS + PS + text + "<i>&#xFF08;FIDT&#x7535;&#x53F0;&#x62A5;&#x9053;&#xFF09;</i>" + PE + DIVE;
        
        String pic = DIVS + PS + IMG + PE + DIVE;
        
        System.out.println(HEAD + pic + para + REAR);
    }
}
