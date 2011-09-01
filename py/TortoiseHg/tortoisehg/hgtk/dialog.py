# Copyright (C) 2006 by Szilveszter Farkas (Phanatic) <szilveszter.farkas@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import gtk
from tortoisehg.util.i18n import _
from tortoisehg.util import hglib
from tortoisehg.hgtk import gtklib

def entry_dialog(parent, msg, visible=True, default='', respfunc=None):
    """ Allow a user to enter a text string (username/password)
    :param message: the message you want to display.
    :param visible: should reponse be visible to user
    :param default: default response text
    :param respfunc: callback function for when dialog exits
    :returns if respfunc returns dialog, else return response text
    """
    buttons = (gtk.STOCK_OK, gtk.RESPONSE_OK,
            gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
    dialog = gtk.Dialog(parent=parent, flags=gtk.DIALOG_MODAL,
            buttons=buttons)
    dialog.set_title(_('TortoiseHg Prompt'))
    dialog.set_has_separator(False)
    entry = gtk.Entry()
    entry.set_text(default or '')
    entry.set_visibility(visible)
    entry.set_activates_default(True)
    lbl = gtk.Label(hglib.toutf(msg))
    lbl.set_alignment(0, 0.5)
    dialog.vbox.pack_start(lbl, True, True, 6)
    dialog.vbox.pack_start(entry, False, False, 6)
    dialog.set_default_response(gtk.RESPONSE_OK)
    dialog.show_all()
    if respfunc:
        dialog.connect('response', respfunc)
        dialog.entry = entry
        return dialog
    else:
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            text = entry.get_text()
        else:
            text = None
        dialog.destroy()
        return text

# TODO: Deprecate and remove these

def _message_dialog(parent, type, primary, secondary, buttons=gtk.BUTTONS_OK,
                    title="TortoiseHg"):
    """ Display a given type of MessageDialog with the given message.

    :param type: message dialog type

    :param message: the message you want to display.
    """
    dialog = gtklib.MessageDialog(parent, flags=gtk.DIALOG_MODAL, type=type,
                               buttons=buttons)
    dialog.set_title(title)
    dialog.set_markup('<big><b>' + primary + '</b></big>')
    dialog.format_secondary_text(secondary)
    dialog.set_position(gtk.WIN_POS_MOUSE)
    response = dialog.run()
    dialog.destroy()
    return response

def error_dialog(parent, primary, secondary):
    """ Display an error dialog with the given message. """
    return _message_dialog(parent, gtk.MESSAGE_ERROR, primary, secondary)

def info_dialog(parent, primary, secondary):
    """ Display an info dialog with the given message. """
    return _message_dialog(parent, gtk.MESSAGE_INFO, primary, secondary)

def warning_dialog(parent, primary, secondary):
    """ Display a warning dialog with the given message. """
    return _message_dialog(parent, gtk.MESSAGE_WARNING, primary, secondary)
