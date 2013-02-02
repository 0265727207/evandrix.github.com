//
//  ShaderAppDelegate.h
//  Shader
//
//  Created by Noel on 8/21/09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import <UIKit/UIKit.h>

@class EAGLView;

@interface ShaderAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    EAGLView *glView;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet EAGLView *glView;

@end

