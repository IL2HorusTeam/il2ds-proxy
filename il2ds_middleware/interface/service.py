# -*- coding: utf-8 -*-

from zope.interface import Interface


class IPilotService(Interface):

    """Interface for creating pilots-monitoring services."""

    def user_joined(self, info):
        """
        Process 'user joined server' event.

        Input:
        `info`  # An object with information about user's callsign, server
                # channel number and remote IP address.
        """

    def user_left(self, info):
        """
        Process 'user left server' event.

        Input:
        `info`  # An object with information about user's callsign, server
                # channel number, remote IP address and reason of
                # disconnection.
        """

    def user_chat(self, info):
        """
        Process 'user sent message to chat' event.

        Input:
        `info`  # A tuple with information about user's callsign and body of
                # the message.
        """

    def seat_occupied(self, info):
        """
        Process 'user occupied seat' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number and position on map.
        """

    def selected_army(self, info):
        """
        Process 'user selected army' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign, army name and position on map.
        """

    def went_to_menu(self, info):
        """
        Process 'user went to refly menu' event.

        Input:
        `info`  # An object with information about event's time, and user's
                # callsign.
        """

    def weapons_loaded(self, info):
        """
        Process 'user loaded weapons' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign, selected aircraft, its loadout and fuel percentage.
        """

    def was_killed(self, info):
        """
        Process 'crew member was killed' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number and position on map.
        """

    def was_killed_by_user(self, info):
        """
        Process 'crew member was killed by user' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number, attacker's callsign,
                # aircraft and position on map.
        """

    def took_off(self, info):
        """
        Process 'user took off' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign, aircraft and position on map.
        """

    def landed(self, info):
        """
        Process 'user landed' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign, aircraft and position on map.
        """

    def crashed(self, info):
        """
        Process 'user crashed' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign, aircraft and position on map.
        """

    def damaged_self(self, info):
        """
        Process 'user damaged himself' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, position on map.
        """

    def was_damaged_by_user(self, info):
        """
        Process 'user was damaged by user' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, attacker's callsign and aircraft,
                # position on map.
        """

    def was_damaged_on_ground(self, info):
        """
        Process 'user was damaged on the ground' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, position on map.
        """

    def shot_down_self(self, info):
        """
        Process 'user shot down himself' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, position on map.
        """

    def was_shot_down_by_user(self, info):
        """
        Process 'user was shot down by user' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, attacker's callsign and aircraft,
                # position on map.
        """

    def was_shot_down_by_static(self, info):
        """
        Process 'user was shot down by static object' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, attacking object's name, position on
                # map.
        """

    def toggle_wingtip_smokes(self, info):
        """
        Process 'user toggled wingtip smokes' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign, aircraft, wingtip smokes state value and position
                # on map.
        """

    def toggle_landing_lights(self, info):
        """
        Process 'user toggled landing lights' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign, aircraft, landing lights state value and position
                # on map.
        """

    def bailed_out(self, info):
        """
        Process 'crew member bailed out' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number and position on map.
        """

    def parachute_opened(self, info):
        """
        Process 'crew member's parachute opened' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number and position on map.
        """

    def was_captured(self, info):
        """
        Process 'crew member was captured' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number and position on map.
        """

    def was_wounded(self, info):
        """
        Process 'crew member was wounded' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number and position on map.
        """

    def was_heavily_wounded(self, info):
        """
        Process 'crew member was heavily wounded' event.

        Input:
        `info`  # An object with information about event's time, user's
                # callsign and aircraft, seat number and position on map.
        """


class IObjectsService(Interface):

    """Interface for creating objects-monitoring services."""

    def building_destroyed_by_user(self, info):
        """
        Process 'building was destroyed by user' event.

        Input:
        `info`  # An object with information about event's time, building's
                # name, user's callsign and aircraft, position on map.
        """

    def tree_destroyed_by_user(self, info):
        """
        Process 'tree was destroyed by user' event.

        Input:
        `info`  # An object with information about event's time, tree's
                # name, user's callsign and aircraft, position on map.
        """

    def static_destroyed_by_user(self, info):
        """
        Process 'static object was destroyed by user' event.

        Input:
        `info`  # An object with information about event's time, object's
                # name, user's callsign and aircraft, position on map.
        """

    def bridge_destroyed_by_user(self, info):
        """
        Process 'bridge was destroyed by user' event.

        Input:
        `info`  # An object with information about event's time, bridge's
                # name, user's callsign and aircraft, position on map.
        """


class IMissionService(Interface):

    """Interface for creating mission-monitoring services."""

    def on_status_info(self, info):
        """
        Process incoming information about mission's status.

        Input:
        `info`  # An object with information about mission's status and name.
        """

    def was_won(self, info):
        """
        Process 'current mission was won by an army' event.

        Input:
        `info`  # An object with information about event's date, time and
                # army's name.
        """

    def target_end(self, info):
        """
        Process event of target's success or failure.

        Input:
        `info`  # An object with information about target's number and result.
        """
