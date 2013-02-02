//
//  RootViewController.h
//  IOSBoilerplate
//
//  Created by Alberto Gimeno Brieba on 08/09/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "BaseViewController.h"

@interface RootViewController : BaseViewController <UITableViewDelegate, UITableViewDataSource> {
    
}

@property (nonatomic, retain) IBOutlet UITableView* table;

@end
