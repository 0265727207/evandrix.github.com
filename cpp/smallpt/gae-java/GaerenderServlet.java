package gaerender;

import java.io.IOException;
import javax.servlet.http.*;

@SuppressWarnings("serial")
public class GaerenderServlet extends HttpServlet {
	public void doGet(HttpServletRequest req, HttpServletResponse resp)
			throws IOException {
		
		try
		{
			int w = Integer.parseInt(req.getParameter("w"));
			int h = Integer.parseInt(req.getParameter("h"));
			int x = Integer.parseInt(req.getParameter("x"));
			int y = Integer.parseInt(req.getParameter("y"));
			int pixels = Integer.parseInt(req.getParameter("pixels"));
			int samples = Integer.parseInt(req.getParameter("samples"));
			
			Sample sample = new Sample();
			Vec v[] = sample.Get(w, h, x, y, pixels, samples);
			
			resp.setContentType("text/plain");
			for(int i = 0; i < v.length; i++)
			{
				resp.getWriter().println(v[i]);
			}
		}
		catch (Exception e)
		{
			resp.setContentType("text/plain");
			resp.getWriter().println("Error");
		}
	}
}
