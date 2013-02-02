//
//  EAGLView.h
//  Shader
//
//  Created by Noel on 8/21/09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//


#import <UIKit/UIKit.h>
#import <OpenGLES/EAGL.h>
#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>

/*
This class wraps the CAEAGLLayer from CoreAnimation into a convenient UIView subclass.
The view content is basically an EAGL surface you render your OpenGL scene into.
Note that setting the view non-opaque will only work if the EAGL surface has an alpha channel.
*/
@interface EAGLView : UIView {
    
@private
    /* The pixel dimensions of the backbuffer */
    GLint backingWidth;
    GLint backingHeight;
    
    EAGLContext *context;   
    GLuint viewRenderbuffer, viewFramebuffer;
    GLuint depthRenderbuffer;
    
	int m_shaderProgram; 
	int m_a_positionHandle;
	int m_a_colorHandle;
	int m_u_mvpHandle;	
	
	float m_angle;
	
    NSTimer *animationTimer;
    NSTimeInterval animationInterval;
}

@property NSTimeInterval animationInterval;

- (void)startAnimation;
- (void)stopAnimation;
- (void)drawView;

@end
