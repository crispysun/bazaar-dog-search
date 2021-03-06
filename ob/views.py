from django.shortcuts import render
from django.http import HttpResponse
import base64
from django.conf import settings


def image(request):
    if settings.DEBUG is True:
        image_data = b'iVBORw0KGgoAAAANSUhEUgAAACoAAAAqBAMAAAA37dRoAAAAG1BMVEX//wAAAAAzMwBmZgD//zOZmQDMzADMzDOZmTNXxfsYAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gMJCx41I1cxbgAAALtJREFUKM/t0k0OgjAQBeAGSt06RdClFQ9ArHFd8GcNngAlegHj/R1BzQCzceHO2ZB8eem8AkL851cTVJz6KadqwqlM2INZlRHbYTygvd2UxSAHALojayxlUEmxWihckiECOfZUbKM2SrOZNuGtQZr14TNzssu8UTui5ctgSnvlrVpI+/0xOgLXuUSjS9lRJe+IMxdA0Vumr8ILc/rG5E6YGB+VR7KHy2rR1j/SOyTW2mfqHHMfoq6+/n8e/oUU2qrAu5AAAAAASUVORK5CYII='
    elif settings.DEV is True:
        image_data = b'iVBORw0KGgoAAAANSUhEUgAAACoAAAAqBAMAAAA37dRoAAAAElBMVEUz//8AAAAAMzMAZmYzzMwzmZk9wIupAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+IDCQsuLnZ0znEAAACkSURBVCjP7ZIxFsIgEEQJbHqXhF7MBfLEA6CYnnj/w7gJ0bcQmhR2bvnfMDMLCPGfX03ra1SNNQqnqsVwgJpqh71v625z3EFE1BmhmmCJMoMggEIazOk9KpOknDbadmGFnCr8zpll2Q/MKswbw55TmajDsexPUsB8rS0poyAmgoaOxCJMP4XsZHFjdkn3kmlhul5S/RfXDc65RfXoaw8R/OH/8wagEhAN51rfnQAAAABJRU5ErkJggg=='
    elif settings.ONION is True:
        image_data = b"iVBORw0KGgoAAAANSUhEUgAAACoAAAAqAgMAAAC4rSHIAAAADFBMVEUODAxwWXCqh6n/yv1d/+DfAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gIRDBYPgAAikQAAAJJJREFUGNNj+A8HHxiGGvvffgT7bz2SuD2SenkkdjwSWx+r+qspcDP/MTBA7foOpJkh7PmP/h+AsdsvApVA2QcYJ8DZFxiAgB3C/gBi80PYP0BsfQj7D5AZUA9h/wWyH8D8BTTlA4w9gUH+wX4Iu4GB+6+MPVT8g/3/PxDxf0sY7P9/haj/Ihq6//9lpPCZjScMAQuZj3KzxzFIAAAAAElFTkSuQmCC"
    else:
        image_data = b'iVBORw0KGgoAAAANSUhEUgAAACoAAAAqAgMAAAC4rSHIAAAADFBMVEUHBwdfX1+ZmZn+/v43scdGAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gMJCxsm2p6E9QAAAJNJREFUGNNj+A8HHxiGGvvffgT7bz2SuD2Sen0kdjx2cST1TyvgZv5jYIDa9f3/FwZmCHv+p/8HYOzuS/8ZYOwDjBPg7AsMQMAOYX8Bsfkh7B8gtj6E/QfInFAPYQMtYngA8xfQlA8w9gIG/Qf7IewGBu6/svZQ8S/2//9AxZcy2P//CVH/RTR0///LSOEzG08YAgCBS5Aw0fodwAAAAABJRU5ErkJggg=='
    return HttpResponse(base64.decodebytes(image_data), content_type="image/png")

def profile_image(request):
    if settings.DEBUG is True:
        image_data = b'iVBORw0KGgoAAAANSUhEUgAAACoAAAAqBAMAAAA37dRoAAAAG1BMVEX//wAAAADMzAAzMwCZmQBmZgD//zPMzDOZmTMQUIQZAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gMJCx8mvvJB8QAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAA2klEQVQoz+WSwQ6CMAyGF1DObAPP1BjPEA3nYdQzGLkT4wOAxuDdFxe2sU1YYjzbw9J86dr+bRH6R/PayEIzTKfQwRinE3rvKLWFWoI5DcY04Zj17mWt6OzF8Xl/6N7tTvEGG8ZUtEmJEmfS02cbwmg1akNY9IUWVpoZVOcFayzgPnP4uJkqEFCg7bLiBXItOYBwSEV0NQJilHOzXJECkdpLnaKIYSH11ImiSQ6+9KpsoB6tQPob5MZynwlxilrsO0Cu/OWUDLBwnww1vmrtetTz821Xt6p/u9I3oLsjGyZscpMAAAAASUVORK5CYII='
    elif settings.DEV is True:
        image_data = b'iVBORw0KGgoAAAANSUhEUgAAACoAAAAqBAMAAAA37dRoAAAAElBMVEUz//8AAAAzzMwAMzMzmZkAZmZdC+ZMAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+IDCQsuHcmkr2cAAAAdaVRYdENvbW1lbnQAAAAAAENyZWF0ZWQgd2l0aCBHSU1QZC5lBwAAAMNJREFUKM/l0ksOgyAQANAJtnsR3TNo95L2ANDPXpt6/6tUYQSqJE3XnYUxL8N8FIC/DCUzaLnYI+Oc9zttZxW51Eyy03qr2rFx5+Iwh5vj1/0xPy/X4MiTMCE71eqzIcUzp2I7hg/5Rces2kQhO7BMdKncnFS6BaBAoZRvMEStsVlLxd1shf5THtN2Y4+UwqdYYtaS9pE6qB6Cgg0qAOn9DAX9QqYrNvrh2xoKOsUmg9S5M7DWWv5G3EiXuUvXyd8u6RsmmBuBxXqLdAAAAABJRU5ErkJggg=='
    elif settings.ONION is True:
        image_data = b"iVBORw0KGgoAAAANSUhEUgAAACoAAAAqAgMAAAC4rSHIAAAADFBMVEUHBwZuWG6ti67/yf0FEwXuAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gIRDBUDops9eQAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAArUlEQVQY08XQIQ4CMRAF0N/dBEgQawkGi8PiyhHwXATX5RqgURhuUI7AEdagMCWpqNh06E7T7SYELKNeRvzkf1B/Bv/zJdsh20D2rlEle6Ds/4AYGIq8Zj+A0RlCc36N7sbshl2wzeAfXf20Hdh9eJosjsmTuaZNzHezBdGtjF6uiO6Imetgs1XsfShsrtnWsY1TRK+WXdhQ8NDKzrs6FD85Nj27FazM23r9dfM3D5lhVvd+cZsAAAAASUVORK5CYII="
    else:
        image_data = b'iVBORw0KGgoAAAANSUhEUgAAACoAAAAqAgMAAAC4rSHIAAAADFBMVEUEBARbW1uhoaH///88Kn54AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gMJCx0ZOqIOTgAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAoUlEQVQY08XQsQ3CMBAF0B+MoAApI7AAEgtEMiOwAYsgJetQsULEBBT00KdxJBcpTjL2HdhXITquetW/+4eQx+F/vhR7FD9hszvU2YBRrpTRfnwHFmfMJL9DmhX7xjZsx14q11/tlSdl0p6jerx30XoTwl7yaRvdy96p2aVDJLOJJd2hZZ+SXbEntqPYaxQbHwteySYf++hBHIbU3Nuffv4CXElkPsRsAuEAAAAASUVORK5CYII='
    return HttpResponse(base64.decodebytes(image_data), content_type="image/png")

# Create your views here.
