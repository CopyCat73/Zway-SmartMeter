/*** SmartMeter Z-Way module *******************************************

Version: 1.00
(c) CopyCatz, 2015
-----------------------------------------------------------------------------
Author: CopyCatz <copycat73@outlook.com>
Description: SmartMeter device status module

******************************************************************************/

function SmartMeter(id, controller) {
    // Call superconstructor first (AutomationModule)
    SmartMeter.super_.call(this, id, controller);
    
    
}

inherits(SmartMeter, AutomationModule);

_module = SmartMeter;

// ----------------------------------------------------------------------------
// --- Module instance initialized
// ----------------------------------------------------------------------------

SmartMeter.prototype.init = function (config) {
    SmartMeter.super_.prototype.init.call(this, config);

    var self = this;
    this.langFile = self.controller.loadModuleLang("SmartMeter");
    var devicename = self.config.devicename.toString();
    var devicescale = self.config.devicescale.toString();
    
    this.vDev = this.controller.devices.create({
        deviceId: "SmartMeter_" + this.id,
        defaults: {
            metrics : {
                level: 0
            }
        },
        overlay: {
            deviceType: "sensorMultilevel",
            metrics : {
                probeTitle: self.langFile.title,
                icon: '/ZAutomation/api/v1/load/modulemedia/SmartMeter/green.png',
                scaleTitle: devicescale,
                title: devicename
            }
        },
        handler:  function (command, args) {
          
            var intLevel = parseInt(args['level']);
            this.set("metrics:level", intLevel);
            if (intLevel >= parseInt(self.config.high_threshold.toString())) {
                this.set('metrics:icon', '/ZAutomation/api/v1/load/modulemedia/SmartMeter/red.png');
            }
            else if (intLevel >= parseInt(self.config.medium_threshold.toString())) {
                this.set('metrics:icon', '/ZAutomation/api/v1/load/modulemedia/SmartMeter/yellow.png');
            }
            else {
                this.set('metrics:icon', '/ZAutomation/api/v1/load/modulemedia/SmartMeter/green.png');
            }
        },
        moduleId: this.id
    })    
};

SmartMeter.prototype.stop = function () {
    
    if (this.vDev) {
        this.controller.devices.remove(this.vDev.id);
        this.vDev = null;
    }

    SmartMeter.super_.prototype.stop.call(this);
};



// ----------------------------------------------------------------------------
// --- Module methods
// ----------------------------------------------------------------------------



