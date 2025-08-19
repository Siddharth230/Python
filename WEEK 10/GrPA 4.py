class Time:
    """
    A class to represent time and convert it from seconds into
    different formats (minutes, hours, days).
    """

    def __init__(self, time: int):
        """
        Initializes the Time object.

        Args:
            time (int): The total time in seconds.
        """
        self.time = time

    def seconds_to_minutes(self) -> str:
        """
        Converts the total seconds into minutes and seconds.

        Returns:
            A string formatted as "<minutes> min <seconds> sec".
        """
        # There are 60 seconds in a minute.
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes} min {seconds} sec"

    def seconds_to_hours(self) -> str:
        """
        Converts the total seconds into hours, minutes, and seconds.

        Returns:
            A string formatted as "<hours> hrs <minutes> min <seconds> sec".
        """
        # Make a local copy to modify
        remaining_time = self.time

        # There are 3600 seconds (60 * 60) in an hour.
        hours = remaining_time // 3600
        remaining_time %= 3600

        # There are 60 seconds in a minute.
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        return f"{hours} hrs {minutes} min {seconds} sec"

    def seconds_to_days(self) -> str:
        """
        Converts the total seconds into days, hours, minutes, and seconds.

        Returns:
            A string formatted as "<days> days <hours> hrs <minutes> min <seconds> sec".
        """
        # Make a local copy to modify
        remaining_time = self.time

        # There are 86400 seconds (24 * 60 * 60) in a day.
        days = remaining_time // 86400
        remaining_time %= 86400

        # There are 3600 seconds in an hour.
        hours = remaining_time // 3600
        remaining_time %= 3600

        # There are 60 seconds in a minute.
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        return f"{days} days {hours} hrs {minutes} min {seconds} sec"
