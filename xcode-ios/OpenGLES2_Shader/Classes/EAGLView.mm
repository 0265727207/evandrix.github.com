#import "EAGLView.h"
#include "Matrix4x4.h"

#import <QuartzCore/QuartzCore.h>
#import <OpenGLES/EAGLDrawable.h>
#include <OpenGLES/ES2/gl.h>


#define USE_DEPTH_BUFFER 0

namespace
{

bool ReadFile(uint8_t* buffer, int bufferSize, NSString* filename)
{
	memset(buffer, 0, bufferSize);

	NSString* pathStr = [[NSString alloc] initWithFormat:@"%@/%@", [[NSBundle mainBundle] resourcePath], filename];
	const char* path = [pathStr cStringUsingEncoding:NSASCIIStringEncoding];
	FILE* fin = fopen(path, "ra");
	if (fin == NULL)
		return false;
	[pathStr release];

	fread(buffer, 1, bufferSize, fin);

	fclose(fin);
	return true;
}




int LoadShader (GLenum type, const uint8_t* source)
{
	const unsigned int shader = glCreateShader(type);
	if (shader == 0)
		return 0;

	glShaderSource(shader, 1, (const GLchar**)&source, NULL);
	glCompileShader(shader);

	int success;
	glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
	if (success == 0)
	{
		char errorMsg[2048];
		glGetShaderInfoLog(shader, sizeof(errorMsg), NULL, errorMsg);
		printf("Compile error: %s\n", errorMsg);
		glDeleteShader(shader);
		return 0;
	}

   return shader;
}


}



// A class extension to declare private methods
@interface EAGLView ()

@property (nonatomic, retain) EAGLContext *context;
@property (nonatomic, assign) NSTimer *animationTimer;

- (BOOL) createFramebuffer;
- (void) destroyFramebuffer;

@end


@implementation EAGLView

@synthesize context;
@synthesize animationTimer;
@synthesize animationInterval;


// You must implement this method
+ (Class)layerClass {
    return [CAEAGLLayer class];
}



- (bool) compileShader
{
	uint8_t buffer[1024];

	if (!ReadFile(buffer, sizeof(buffer), @"VertexShader.txt"))
		return false;
	const int vertexShader = LoadShader (GL_VERTEX_SHADER, buffer);
	if (vertexShader == 0)
		return false;

	if (!ReadFile(buffer, sizeof(buffer), @"FragmentShader.txt"))
		return false;
	const int fragmentShader = LoadShader (GL_FRAGMENT_SHADER, buffer);
	if (fragmentShader == 0)
		return false;

	m_shaderProgram = glCreateProgram();
	if (m_shaderProgram == 0)
      return false;

	glAttachShader(m_shaderProgram, vertexShader);
	glAttachShader(m_shaderProgram, fragmentShader);
	glLinkProgram(m_shaderProgram);
	int linked;
	glGetProgramiv(m_shaderProgram, GL_LINK_STATUS, &linked);
	if (linked == 0) 
	{
		glDeleteProgram(m_shaderProgram);
		return false;
	}


	m_a_positionHandle = glGetAttribLocation(m_shaderProgram, "a_position");
	m_a_colorHandle = glGetAttribLocation(m_shaderProgram, "a_color");
	
	m_u_mvpHandle = glGetUniformLocation(m_shaderProgram, "u_mvpMatrix");

	return true;
}


- (id)initWithCoder:(NSCoder*)coder {
    
    if ((self = [super initWithCoder:coder])) {
        // Get the layer
        CAEAGLLayer *eaglLayer = (CAEAGLLayer *)self.layer;
        
        eaglLayer.opaque = YES;
        eaglLayer.drawableProperties = [NSDictionary dictionaryWithObjectsAndKeys:
                                        [NSNumber numberWithBool:NO], kEAGLDrawablePropertyRetainedBacking, kEAGLColorFormatRGBA8, kEAGLDrawablePropertyColorFormat, nil];
        
		// Make sure this is the right version!
        context = [[EAGLContext alloc] initWithAPI:kEAGLRenderingAPIOpenGLES2];
        if (!context || ![EAGLContext setCurrentContext:context]) {
            [self release];
            return nil;
        }
        
		const bool ok = [self compileShader];
		assert(ok);
		
        animationInterval = 1.0 / 60.0;
    }
    return self;
}


- (void)drawView 
{
    const GLfloat squareVertices[] = {
        -0.5f, -0.5f,
        0.5f,  -0.5f,
        -0.5f,  0.5f,
        0.5f,   0.5f,
    };
    const GLfloat squareColors[] = {
        1, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 1,
        1, 0, 1, 1,
    };
    
	
	m_angle += 0.02f;
				
	Matrix4x4 proj;
	Matrix4x4Utils::SetOrtho(proj, -1.0f, 1.0f, -1.5f, 1.5f, -1.0f, 1.0f);
	Matrix4x4 rot;
	Matrix4x4Utils::SetRotZ(rot, m_angle);
	Matrix4x4 mvp;
	Matrix4x4Utils::Mul(mvp, rot, proj);
	
    [EAGLContext setCurrentContext:context];
    
    glBindFramebufferOES(GL_FRAMEBUFFER_OES, viewFramebuffer);
    glViewport(0, 0, backingWidth, backingHeight);

    glClearColor(0.5f, 0.5f, 0.5f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    	
	glUseProgram(m_shaderProgram);
	
	glVertexAttribPointer(m_a_positionHandle, 2, GL_FLOAT, GL_FALSE, 0, squareVertices);
	glEnableVertexAttribArray(m_a_positionHandle);
	glVertexAttribPointer(m_a_colorHandle, 4, GL_FLOAT, GL_FALSE, 0, squareColors);
	glEnableVertexAttribArray(m_a_colorHandle);
	glUniformMatrix4fv(m_u_mvpHandle, 1, GL_FALSE, (GLfloat*)&mvp.m[0] );
   
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
		
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, viewRenderbuffer);
    [context presentRenderbuffer:GL_RENDERBUFFER_OES];
}


- (void)layoutSubviews {
    [EAGLContext setCurrentContext:context];
    [self destroyFramebuffer];
    [self createFramebuffer];
    [self drawView];
}


- (BOOL)createFramebuffer {
    
    glGenFramebuffersOES(1, &viewFramebuffer);
    glGenRenderbuffersOES(1, &viewRenderbuffer);
    
    glBindFramebufferOES(GL_FRAMEBUFFER_OES, viewFramebuffer);
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, viewRenderbuffer);
    [context renderbufferStorage:GL_RENDERBUFFER_OES fromDrawable:(CAEAGLLayer*)self.layer];
    glFramebufferRenderbufferOES(GL_FRAMEBUFFER_OES, GL_COLOR_ATTACHMENT0_OES, GL_RENDERBUFFER_OES, viewRenderbuffer);
    
    glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_WIDTH_OES, &backingWidth);
    glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_HEIGHT_OES, &backingHeight);
    
    if (USE_DEPTH_BUFFER) {
        glGenRenderbuffersOES(1, &depthRenderbuffer);
        glBindRenderbufferOES(GL_RENDERBUFFER_OES, depthRenderbuffer);
        glRenderbufferStorageOES(GL_RENDERBUFFER_OES, GL_DEPTH_COMPONENT16_OES, backingWidth, backingHeight);
        glFramebufferRenderbufferOES(GL_FRAMEBUFFER_OES, GL_DEPTH_ATTACHMENT_OES, GL_RENDERBUFFER_OES, depthRenderbuffer);
    }
    
    if(glCheckFramebufferStatusOES(GL_FRAMEBUFFER_OES) != GL_FRAMEBUFFER_COMPLETE_OES) {
        NSLog(@"failed to make complete framebuffer object %x", glCheckFramebufferStatusOES(GL_FRAMEBUFFER_OES));
        return NO;
    }
    
    return YES;
}


- (void)destroyFramebuffer {
    
    glDeleteFramebuffersOES(1, &viewFramebuffer);
    viewFramebuffer = 0;
    glDeleteRenderbuffersOES(1, &viewRenderbuffer);
    viewRenderbuffer = 0;
    
    if(depthRenderbuffer) {
        glDeleteRenderbuffersOES(1, &depthRenderbuffer);
        depthRenderbuffer = 0;
    }
}


- (void)startAnimation {
    self.animationTimer = [NSTimer scheduledTimerWithTimeInterval:animationInterval target:self selector:@selector(drawView) userInfo:nil repeats:YES];
}


- (void)stopAnimation {
    self.animationTimer = nil;
}


- (void)setAnimationTimer:(NSTimer *)newTimer {
    [animationTimer invalidate];
    animationTimer = newTimer;
}


- (void)setAnimationInterval:(NSTimeInterval)interval {
    
    animationInterval = interval;
    if (animationTimer) {
        [self stopAnimation];
        [self startAnimation];
    }
}


- (void)dealloc {
    
    [self stopAnimation];
    
    if ([EAGLContext currentContext] == context) {
        [EAGLContext setCurrentContext:nil];
    }
    
    [context release];  
    [super dealloc];
}

@end
