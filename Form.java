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
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
            <title>""" + title + 
        """
        </title>
        </head>
        <body>
            <div>
                    <a href="https://maxchen32.github.io/fidt" title="FIDT-&#x9996;&#x9875;">
                            <img src="../pic/logo.svg" alt="FIDT_logo" height="200" width="200">
                    </a><br>
                    <strong style="color: red">&#x672C;&#x9875;&#x9762;&#x4EC5;&#x4E3A;&#x73A9;&#x7B11;&#xFF0C;&#x5E76;&#x65E0;&#x6076;&#x610F;</strong><br>
            </div>
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
        
        final String INDENT = "&emsp;&emsp;";
                
        
        String IMG = "<img id=\"txtpic\" src=\"../pic/" + piclink + "\" />";
        
        String para = DIVS + PS + INDENT + text + "<i>&#xFF08;FIDT&#x7535;&#x53F0;&#x62A5;&#x9053;&#xFF09;</i>" + PE + DIVE;
        
        String pic = DIVS + PS + IMG + PE + DIVE;
        
        System.out.println(HEAD + pic + para + REAR);
    }
}
