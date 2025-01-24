#ifndef _PYSKY_H_
#define _PYSKY_H_

#include <pybind11/embed.h>
#include "squirrel/Sky.h"

namespace py = pybind11;

class PySky
{
    
public:
    
    static void setWeather(nonut::Int value)                    { nonut::Sky::get()->weather = value; }
    static nonut::Int getWeather()                              { return nonut::Sky::get()->weather; }
    static void setRaining(nonut::Bool value)                   { nonut::Sky::get()->raining = value; }
    static nonut::Bool getRaining()                             { return nonut::Sky::get()->raining; }
    static void setRenderLightning(nonut::Bool value)           { nonut::Sky::get()->renderLightning = value; }
    static nonut::Bool getRenderLightning()                     { return nonut::Sky::get()->renderLightning; }
    static void setWindScale(nonut::Float value)                { nonut::Sky::get()->windScale = value; }
    static nonut::Float getWindScale()                          { return nonut::Sky::get()->windScale; }
    static void setDontRain(nonut::Bool value)                  { nonut::Sky::get()->dontRain = value; }
    static nonut::Bool getDontRain()                            { return nonut::Sky::get()->dontRain; }
    
    static void setRainStartTime(nonut::Int h, nonut::Int m)    { nonut::Sky::get()->setRainStartTime(h, m); }
    static void setRainStopTime(nonut::Int h, nonut::Int m)     { nonut::Sky::get()->setRainStopTime(h, m); }
    static py::dict getRainStartTime()                          { return nonut::Sky::get()->getRainStartTime().data; }
    static py::dict getRainStopTime()                           { return nonut::Sky::get()->getRainStopTime().data; }
};

#endif