# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class CalDraw:
    """ A class to draw a calendar.

        Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
    """
    def __init__(self, parent: 'Window') -> None:
        """ Default class constructor

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def AddSelect(self, list, cfont=None, cbackgrd=None) -> None:
        """ Add a selection of days.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def Center(self) -> None:
        """ Calculate the dimensions in the center of the drawing area.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DefParms(self) -> None:
        """ Setup the default parameters.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawBorder(self, DC, transparent=False) -> None:
        """ Draw a border around the outside of the main display rectangle.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawCal(self, DC, sel_lst=[]) -> None:
        """ Draw the calendar.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawDayText(self, DC, key) -> None:
        """ Draw the day text.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawFocusIndicator(self, DC: 'DC') -> None:
        """ Draw the focus indicator

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawGrid(self, DC: 'DC') -> None:
        """ Calculate and draw the grid lines.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawMonth(self, DC: 'DC') -> None:
        """ Draw the month and year titles.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawNum(self, DC: 'DC') -> None:
        """ Draw the day numbers

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawNumVal(self) -> None:
        """ Draw the numeric values.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawSel(self, DC: 'DC') -> None:
        """ Highlight selected days.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawWeek(self, DC: 'DC') -> None:
        """ Draw the week days.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetCal(self) -> None:
        """ Get the calendar days.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetColor(self, name: Any) -> None:
        """ Get a color.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetOffset(self) -> None:
        """ Get the offset position.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetRect(self) -> None:
        """ Get the display rectangle list of the day grid.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def InitScale(self) -> None:
        """ Set the default scale values.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def InitValues(self) -> None:
        """ Default dimensions of various elements of the calendar.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetCal(self, year, month) -> None:
        """ Calculate the calendar days and offset position.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetColor(self, name, value) -> None:
        """ Set a color.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetMarg(self, xmarg, ymarg) -> None:
        """ Set the margins.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetPos(self, xpos, ypos) -> None:
        """ Set the position.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetSize(self, size: Any) -> None:
        """ Set the size.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetWeekColor(self, font_color, week_color) -> None:
        """ Set the font and background color of the week title.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetWeekEnd(self, font_color=None, backgrd=None) -> None:
        """ Set the weekend backgrounds.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """



class Calendar(Control):
    """ A calendar control class.

        Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
    """
    def __init__(*args, **kwargs) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def AcceptsFocus(self) -> None:
        """ Can it accept focus?

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def AddSelect(self, list, font_color, back_color) -> None:
        """ Add a selection.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DecMonth(self) -> None:
        """ Decrement the month by 1.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DecYear(self) -> None:
        """ Decrement the year by 1.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DoDrawing(self, DC: 'DC') -> None:
        """ Do the drawing.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DrawFocusIndicator(self, draw: bool) -> None:
        """ Draw the focus indicator or a border.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DrawRect(self, key, bgcolor='WHITE', fgcolor='PINK', width=0) -> None:
        """ Draw a rectangle.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DrawRectOrg(self, key, fgcolor='BLACK', width=0) -> None:
        """ Draw a rectangle.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetColor(self, color: str) -> None:
        """ Get a color.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetDate(self) -> None:
        """ Get the set calendar date.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetDay(self) -> None:
        """ Get the set calendar day.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetDayHit(self, mx, my) -> None:
        """ Find the clicked area rectangle.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetMonth(self) -> None:
        """ Get the set calendar month.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetYear(self) -> None:
        """ Get the set calendar year.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def HideGrid(self) -> None:
        """ Hide the calendar grid.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def HideTitle(self) -> None:
        """ Hide the calendar title.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def IncMonth(self) -> None:
        """ Increment the month by 1.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def IncYear(self) -> None:
        """ Increment the year by 1.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def IsDayInWeekend(self, key: Any) -> None:
        """ Is the day in the weekend

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def MoveDate(self, months=0, years=0) -> None:
        """ Move the current date by a given interval of months/years.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnKeyDown(self, event) -> None:
        """ Key down event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnKillFocus(self, event) -> None:
        """ Kill focus event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnLeftDEvent(self, event) -> None:
        """ Left double mouse click event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnLeftEvent(self, event) -> None:
        """ Left mouse click event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnMiddleDEvent(self, event) -> None:
        """ Middle double mouse click event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnMiddleEvent(self, event) -> None:
        """ Middle mouse click event  handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnPaint(self, event) -> None:
        """ The on paint event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnRightDEvent(self, event) -> None:
        """ Right double mouse click event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnRightEvent(self, event) -> None:
        """ Right mouse click event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnSetFocus(self, event) -> None:
        """ Set focus event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnSize(self, evt) -> None:
        """ The on size event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def ProcessClick(self, event) -> None:
        """ Determine the calendar rectangle click area and draw a selection.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SelectDay(self, key: Any) -> None:
        """ Select the day.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetBusType(self) -> None:
        """ Set the calendar type to âBUSâ.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetColor(self, name, value) -> None:
        """ Set a color.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetCurrentDay(self) -> None:
        """ Set the current day to today.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetDate(self, day, month, year) -> None:
        """ Set a calendar date.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetDay(self, day: Any) -> None:
        """ Set the day.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetDayValue(self, day: int) -> None:
        """ Set the day.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetMargin(self, xmarg, ymarg) -> None:
        """ Set the margins

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetMonth(self, month: int) -> None:
        """ Set the Month.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetNow(self) -> None:
        """ Set the current day.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetSelDay(self, sel: list) -> None:
        """ Set the days to highlight.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetSize(self, set_size: Union[tuple[int, int], 'Size']) -> None:
        """ Set the size.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetTextAlign(self, vert, horz) -> None:
        """ Set the text alignment.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetWeekColor(self, font_color, week_color) -> None:
        """ Set the week title color.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetYear(self, year: int) -> None:
        """ Set the year.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def ShowWeekEnd(self) -> None:
        """ Highlight the weekend.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def TestDay(self, key: Any) -> None:
        """ Test to see if the selection has a date and create event.

            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """



class CalenDlg(Dialog):
    """ A dialog with a calendar control.

        Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
    """
    def __init__(self, parent, month=None, day=None, year=None) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def EvtComboBox(self, event) -> None:
        """ The month combobox event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def MouseClick(self, evt) -> None:
        """ The mouse click event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnCancel(self, event) -> None:
        """ The Cancel event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnMonthSpin(self, event) -> None:
        """ The month spin control event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnOk(self, evt) -> None:
        """ The OK event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnYrSpin(self, event) -> None:
        """ The year spin control event handler.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def ResetDisplay(self) -> None:
        """ Reset the display.

            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """



class PrtCalDraw(CalDraw):
    """ A class to optimize CalDraw for printing.

        Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
    """
    def InitValues(self) -> None:
        """ Set initial values.

            Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
        """

    def SetPreview(self, preview: Any) -> None:
        """ Set the preview.

            Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
        """

    def SetPSize(self, pwidth, pheight) -> None:
        """ Calculate the dimensions in the center of the drawing area.

            Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
        """



