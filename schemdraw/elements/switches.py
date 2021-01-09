''' Switches and buttons '''
from typing import Optional, Literal
import math

from .elements import Element, Element2Term, gap
from ..segments import Segment, SegmentCircle, SegmentArc, SegmentArrow
from ..types import Point
from ..util import linspace

sw_dot_r = .12

ActionType = Optional[Literal['open', 'close']]


class Switch(Element2Term):
    ''' Toggle Switch

        Args:
            action: action arrow ('open' or 'close')
    '''
    def __init__(self, *d, action: ActionType=None, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment(
            [[0, 0], gap, [sw_dot_r*2, .1], [.8, .45], gap, [1, 0]]))
        self.segments.append(SegmentCircle([sw_dot_r, 0], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, 0], sw_dot_r))
        if action == 'open':
            self.segments.append(SegmentArc([.4, .1], width=.5, height=.75,
                                            theta1=-10, theta2=70,
                                            arrow='ccw'))
        if action == 'close':
            self.segments.append(SegmentArc([.4, .25], width=.5, height=.75,
                                            theta1=-10, theta2=70,
                                            arrow='cw'))


class SwitchSpdt(Switch):
    ''' Single-pole double throw switch.

        Args:
            action: action arrow ('open' or 'close')

        Anchors:
            * a
            * b
            * c
    '''
    def __init__(self, *d, action: ActionType=None, **kwargs):
        super().__init__(*d, action=action, **kwargs)
        self.segments.append(SegmentCircle([1-sw_dot_r, .7], sw_dot_r))
        self.anchors['a'] = Point((0, 0))
        self.anchors['b'] = Point((1, 0))
        self.anchors['c'] = Point((1, .7))


class SwitchSpdt2(Element):
    ''' Single-pole double throw switch, throws above and below.

        Args:
            action: action arrow ('open' or 'close')

        Anchors:
            * a
            * b
            * c
    '''
    def __init__(self, *d, action: ActionType=None, **kwargs):
        super().__init__(*d, action=action, **kwargs)
        self.segments.append(Segment([[0, 0], gap, [sw_dot_r*2, .1],
                                      [.7, .25], gap, [1, .4]]))
        self.segments.append(SegmentCircle([sw_dot_r, 0], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, -.4], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, .4], sw_dot_r))
        self.anchors['a'] = Point((0, 0))
        self.anchors['b'] = Point((1, .4))
        self.anchors['c'] = Point((1, -.4))
        if action == 'open':
            self.segments.append(SegmentArc([.35, 0], width=.5, height=.75,
                                            theta1=-10, theta2=70,
                                            arrow='ccw'))
        elif action == 'close':
            self.segments.append(SegmentArc([.3, 0], width=.5, height=.75,
                                            theta1=-10, theta2=70,
                                            arrow='cw'))
        self.params['drop'] = [1, .4]


class Button(Element2Term):
    ''' Push button switch

        Args:
            nc: Normally closed
    '''
    def __init__(self, *d, nc: bool=False, **kwargs):
        super().__init__(*d, **kwargs)
        if nc:
            self.segments.append(Segment(
                [[0, 0], gap, [sw_dot_r, -sw_dot_r-.05],
                 [1-sw_dot_r, -sw_dot_r-.05], gap, [.5, -sw_dot_r-.05],
                 [.5, sw_dot_r+.15], gap, [1, 0]]))
        else:
            self.segments.append(Segment(
                [[0, 0], gap, [sw_dot_r, .3], [1-sw_dot_r, .3],
                 gap, [.5, .3], [.5, .5], gap, [1, 0]]))

        self.segments.append(SegmentCircle([sw_dot_r, 0], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, 0], sw_dot_r))


class SwitchDpst(Element):
    ''' Double-pole single-throw switch

        Args:
            link: Show dotted line linking switch levers

        Anchors:
            * p1
            * p2
            * t1
            * t2
    '''
    def __init__(self, *d, link: bool=True, **kwargs):
        super().__init__(*d, **kwargs)
        yofst = -1
        self.segments.append(Segment([[0, 0], gap, [sw_dot_r*2, .1],
                                      [.8, .45], gap, [1, 0]]))
        self.segments.append(SegmentCircle([sw_dot_r, 0], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, 0], sw_dot_r))
        self.segments.append(Segment([[0, yofst], gap, [sw_dot_r*2, yofst+.1],
                                      [.8, yofst+.45], gap, [1, yofst]]))
        self.segments.append(SegmentCircle([sw_dot_r, yofst], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, yofst], sw_dot_r))
        if link:
            self.segments.append(Segment([[0.5, yofst+.25],
                                          [0.5, 0.2]], ls=':'))
        self.anchors['p1'] = [0, 0]
        self.anchors['t1'] = [1, 0]
        self.anchors['p2'] = [0, yofst]
        self.anchors['t2'] = [1, yofst]


class SwitchDpdt(Element):
    ''' Double-pole double-throw switch

        Args:
            link: Show dotted line linking switch levers

        Anchors:
            * p1
            * p2
            * t1
            * t2
            * t3
            * t4
    '''
    def __init__(self, *d, link: bool=True, **kwargs):
        super().__init__(*d, **kwargs)
        yofst = -1.4
        self.segments.append(Segment([[0, 0], gap, [sw_dot_r*2, .1],
                                      [.7, .25], gap, [1, .4]]))
        self.segments.append(SegmentCircle([sw_dot_r, 0], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, -.4], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, .4], sw_dot_r))
        self.segments.append(Segment([[0, yofst], gap, [sw_dot_r*2, yofst+.1],
                                      [.7, yofst+.25], gap, [1, yofst+.4]]))
        self.segments.append(SegmentCircle([sw_dot_r, yofst], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, yofst-.4], sw_dot_r))
        self.segments.append(SegmentCircle([1-sw_dot_r, yofst+.4], sw_dot_r))
        if link:
            self.segments.append(Segment([[0.5, yofst+.25],
                                          [0.5, 0.2]], ls=':'))
        self.anchors['p1'] = [0, 0]
        self.anchors['t1'] = [1, .4]
        self.anchors['t2'] = [1, -.4]
        self.anchors['p2'] = [0, yofst]
        self.anchors['t3'] = [1, yofst+.4]
        self.anchors['t4'] = [1, yofst-.4]


class SwitchReed(Element2Term):
    ''' Reed Switch '''
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment(
            [[0, 0], [.85, .15], gap, [.8, 0]]))
        
        r = .3
        th = linspace(-math.pi/2, math.pi/2)
        x1 = [-r * math.cos(t) for t in th]  # Left semicircle
        y1 = [r * math.sin(t) for t in th]
        x2 = [1-k for k in x1]  # Right semicircle        

        x = x1 + x2 + [x1[0]]   # Combined
        y = y1 + y1[::-1] + [y1[0]]
        self.segments.append(Segment(list(zip(x, y))))

        
class SwitchRotary(Element):
    ''' Rotary Switch

        Args:
            n: number of contacts
            dtheta: angle in degrees between each contact
            theta0: angle in degrees of first contact
            radius: radius of switch
            arrowlen: length of switch arrow
            arrowcontact: index of contact to point to

        Values for dtheta and theta will be calculated based on `n`
        if not provided.
        
        Anchors:
            * P
            * T[x] for each contact (starting at 1)
    '''
    def __init__(self, *d, 
                 n: int=4, dtheta: float=None, theta0: float=None,
                 radius: float=1, arrowlen: float=0.75,
                 arrowcontact: int=0,
                 **kwargs):
        super().__init__(*d, **kwargs)
        self.params['fill'] = 'bg'
        self.params['zorder'] = 4
        self.segments.append(SegmentCircle((0, 0), sw_dot_r))
        self.anchors['P'] = (0, 0)

        if dtheta is None:
            dtheta = min(35, 360/(n+1))
        
        dtheta = math.radians(dtheta)
        if theta0 is None:
            theta0 = -dtheta * (n-1)/2

        for i in range(n):
            t = theta0 + dtheta * i
            x = radius * math.cos(t)
            y = radius * math.sin(t)
            self.segments.append(SegmentCircle((x, y), sw_dot_r))
            self.anchors[f'T{i+1}'] = (x, y)
        
            if i == arrowcontact:
                arrowx = arrowlen * math.cos(t)
                arrowy = arrowlen * math.sin(t)
                self.segments.append(SegmentArrow((0, 0), (arrowx, arrowy), zorder=2))
