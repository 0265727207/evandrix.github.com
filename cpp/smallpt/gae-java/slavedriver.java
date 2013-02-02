
import java.net.*;
import java.awt.image.BufferedImage;
import java.awt.image.WritableRaster;
import java.io.*;

import javax.imageio.ImageIO;

import gaerender.Vec;

public class slavedriver {
	
	int w, h, samps, PixelsPerRequest;
	int SimultaneousRequests = 5;
	String address = "http://localhost:8888";
	
	slavedriver(int _w, int _h, int _samps, int _PixelsPerRequest)
	{
		w = _w;
		h = _h;
		samps = _samps;
		PixelsPerRequest = _PixelsPerRequest;
	}

	double clamp(double x)
	{
		return x < 0.0 ? 0.0 : x > 1.0 ? 1.0 : x;
	}
	
	int toInt(double x)
	{
		return (int)(Math.pow(clamp(x),1.0/2.2)*255.0+.5);
	}
	
	class Request
	{
		public int x, y, pixels;
		private boolean isComplete;
		private URLConnection con;
		
		public Request(int _x, int _y, int _pixels)
		{
			x = _x;
			y = _y;
			pixels = _pixels;
			isComplete = false;
		}
		
		public void Send()
		{
			try
			{
				URL url = new URL(String.format(address + "/gaerender?w=%d&h=%d&x=%d&y=%d&samples=%d&pixels=%d", w, h, x, y, samps * 4, pixels));
				con = url.openConnection();
				//con.setReadTimeout(1);	// Throw exception after trying to read for 1ms
				System.out.println(String.format("Sending request for %d pixels starting at (%d, %d).", pixels, x, y));
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
		}
		
		public void WriteResults(WritableRaster raster)
		{
			try
			{
				int i = x + y * w;
				
				BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
				String inputLine;
				
				for(int z = 0; (inputLine = in.readLine()) != null; z++)
				{
					Vec v = new Vec(inputLine);
					int a[] = new int[3];
					a[0] = toInt(v.x);
					a[1] = toInt(v.y);
					a[2] = toInt(v.z);
					raster.setPixel(i % w, h - i / w - 1, a);
				}
				in.close();
				
				System.out.println(String.format("Received %d pixels starting at (%d, %d).", PixelsPerRequest, x, y));
				
				isComplete = true;
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
		}
		
		public boolean IsComplete()
		{
			return isComplete;
		}
	}
	
	public void run()
	{
		try
		{
			int x = 0;
			int y = 0;
			
			int RequestCount = (w*h) / PixelsPerRequest;
			if((w*h) % PixelsPerRequest > 0)
			{
				RequestCount += 1;
			}
			
			Request requests[] = new Request[RequestCount];
			
			for(int i = 0, pixel = 0; i < RequestCount; ++i)
			{
				requests[i] = new Request(x, y, PixelsPerRequest);
				pixel += PixelsPerRequest;
				
				if(pixel + PixelsPerRequest > w*h)
				{
					PixelsPerRequest = (w*h) % PixelsPerRequest;				
				}
				
				x = pixel % w;
				y = pixel / w;
			}
			
			String filename = String.format("%s_%dx%d_%dspp.png", "gae", w, h, samps * 4);
			File file = new File(filename);
			
			BufferedImage image = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);
			WritableRaster raster = image.getRaster();
			
			for(int i = 0; i < RequestCount; ++i)
			{
				requests[i].Send();
			}
			
			while(true)
			{
				boolean isComplete = true;
				
				for(int i = 0; i < RequestCount; ++i)
				{
					if(!requests[i].IsComplete())
					{
						isComplete = false;
						requests[i].WriteResults(raster);
					}
				}
				
				if(isComplete)
				{
					break;
				}
			}

			ImageIO.write(image, "png", file);
			
			System.out.println("Done.");
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args)
	{
		int w = 1024;
		int h = 768;
		int samps = 44/4;
		int PixelsPerRequest = w * h;
		
		slavedriver slave = new slavedriver(w, h, samps, PixelsPerRequest);
		slave.run();
	}

}