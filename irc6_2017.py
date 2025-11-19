import math
import numpy as np
from comman import *



class IRC6_2017:
    @staticmethod
    def cl_203_dead_load():
        # Clause 203 Dead Load
        """Returns dead load values for various materials in t/m3 as per IRC:6-2017 Clause 203."""
        dead_load = {}
        dead_load['ashlar_granite'] = 2.7  # t/m3
        dead_load['ashlar_sandstone'] = 2.4  # t/m3
        dead_load['stone_setts_granite'] = 2.6  # t/m3
        dead_load['stone_setts_basalt'] = 2.7  # t/m3
        dead_load['ballast_granite'] = 1.4  # t/m3
        dead_load['ballast_basalt'] = 1.6  # t/m3
        dead_load['brickwork_pressed_cement'] = 2.2  # t/m3
        dead_load['brickwork_common_cement'] = 1.9  # t/m3
        dead_load['brickwork_common_lime'] = 1.8  # t/m3
        dead_load['concrete_asphalt'] = 2.2  # t/m3
        dead_load['concrete_bitumen'] = 1.4  # t/m3
        dead_load['concrete_cement_plain'] = 2.5  # t/m3
        dead_load['concrete_cement_plain_plums'] = 2.5  # t/m3
        dead_load['concrete_cement_reinforced'] = 2.5  # t/m3
        dead_load['concrete_cement_prestressed'] = 2.5  # t/m3
        dead_load['concrete_lime_brick'] = 1.9  # t/m3
        dead_load['concrete_lime_stone'] = 2.1  # t/m3
        dead_load['earth_compacted'] = 2.0  # t/m3
        dead_load['gravel'] = 1.8  # t/m3
        dead_load['macadam_binder'] = 2.2  # t/m3
        dead_load['macadam_rolled'] = 2.6  # t/m3
        dead_load['sand_loose'] = 1.7  # t/m3
        dead_load['sand_wet'] = 1.9  # t/m3
        dead_load['rubble_stone_coursed'] = 2.6  # t/m3
        dead_load['stone_masonry_lime'] = 2.4  # t/m3
        dead_load['water'] = 1.0  # t/m3
        dead_load['wood'] = 0.8  # t/m3
        dead_load['cast_iron'] = 7.2  # t/m3
        dead_load['wrought_iron'] = 7.7  # t/m3
        dead_load['steel'] = 7.8  # t/m3
        return dead_load
    
    @staticmethod
    def cl_204_1_Class70R_vehicle():
        """
        Makes an Class70R vehicle in local coordinates
        Returns a dictionary with keys:
            'x' - list of longitudinal load positions (m)
            'z' - list of transverse load positions (m)
            'wheel_loads' - list of wheel loads (kN)
        """
        # Define units
        front_gap = 0.81 * m
        axle_dist1= 3.960 * m
        axle_dist2= 1.520 * m
        gap_bogie= 2.130 * m
        bogie_axle_dist1= 1.370 * m
        bogie_axle_dist2= 3.050 * m
        rear_gap = 0.91 * m

        # Define wheel loads (kN) for each longitudinal axle position
        # Mapping to the 7 longitudinal positions in `load_positions_x`.
        # Values provided by user (converted to kN):
        # [8, 12, 12, 17, 17, 17, 17]
        wheel_loads = [8 * kN, 12 * kN, 12 * kN, 17 * kN,
                      17 * kN, 17 * kN, 17 * kN]

        # Define longitudinal positions of each axle
        load_positions_x = [
                front_gap,
                front_gap + axle_dist1,
                front_gap + axle_dist1 + axle_dist2,
                front_gap + axle_dist1 + axle_dist2 + gap_bogie,
                front_gap + axle_dist1 + axle_dist2 + gap_bogie + bogie_axle_dist1,
                front_gap + axle_dist1 + axle_dist2 + gap_bogie + bogie_axle_dist1 + bogie_axle_dist2,
                front_gap + axle_dist1 + axle_dist2 + gap_bogie + bogie_axle_dist1 + bogie_axle_dist2 + rear_gap,
                ]
            
        # Transverse position of each wheel
        load_positions_z = [-1.395, 1.395]

        # Spacing between two sucessive class 70R vehicles
        spacing_Class70R = 30.0 * m

        # make a dictonary to return vehicle data
        return {
            'x': load_positions_x,
            'z': load_positions_z,
            'wheel_loads': wheel_loads,
            'spacing_Class70R': spacing_Class70R
        }
    
    @staticmethod
    def cl_204_1_ClassA_vehicle():
        """
        Makes an ClassA vehicle in local coordinates
        Returns a dictionary with keys:
            'x' - list of longitudinal load positions (m)
            'z' - list of transverse load positions (m)
            'wheel_loads' - list of wheel loads (kN)
        """
        # Define units
        front_gap = 0.6 * m
        axle_dist1 = 1.100 * m
        axle_dist2 = 3.200 * m
        axle_dist3 = 1.200 * m
        gap_bogie = 4.300 * m
        bogie_axle_dist = 3.000 * m
        rear_gap = 0.900 * m

       # Define wheel loads (kN) for each longitudinal axle position
       # Mapping to the 8 longitudinal positions in `load_positions_x`.
       # Values provided by user (converted to kN):
       # [2.7, 2.7, 11.4, 11.4, 6.8, 6.8, 6.8, 6.8]
        wheel_loads = [2.7 * kN, 2.7 * kN, 11.4 * kN, 11.4 * kN,
                      6.8 * kN, 6.8 * kN, 6.8 * kN, 6.8 * kN]

        # Define longitudinal positions of each axle
        load_positions_x = [
            front_gap,
            front_gap + axle_dist1,
            front_gap + axle_dist1 + axle_dist2,
            front_gap + axle_dist1 + axle_dist2 + axle_dist3,
            front_gap + axle_dist1 + axle_dist2 + axle_dist3 + gap_bogie,
            front_gap + axle_dist1 + axle_dist2 + axle_dist3 + gap_bogie + bogie_axle_dist,
            front_gap + axle_dist1 + axle_dist2 + axle_dist3 + gap_bogie + bogie_axle_dist + bogie_axle_dist,
            front_gap + axle_dist1 + axle_dist2 + axle_dist3 + gap_bogie + bogie_axle_dist + bogie_axle_dist + bogie_axle_dist + rear_gap,
            ]
        # Transverse position of each wheel
        load_positions_z = [-0.9,0.9]

        # Spacing between two sucessive class A vehicles
        spacing_ClassA = 18.5 * m
   
        # make a dictonary to return vehicle data
        return {
            'x': load_positions_x,
            'z': load_positions_z,
            'wheel_loads': wheel_loads,
            'spacing_ClassA': spacing_ClassA
        }
    
    
    
    @staticmethod
    def table_3(clear_carriageway_width):
        """
        Calculates the minimum clearance values for Class A train vehicles based on given clear carriageway width
        as per IRC:6-2017 Table 3.
        
        Args:
            clear_carriageway_width (float): The clear carriageway width in meters
            
        Returns:
            dict: A dictionary containing calculated clearance values
                 'g' - clearance between outer edges of passing vehicles (in meters)
                 'f' - clearance between outer edge of wheel and roadway face (in millimeters)
                 
        Raises:
            ValueError: If the carriageway width is less than 5.3 meters
        """
        # Check if width is within valid range
        if clear_carriageway_width < 5.3:
            raise ValueError("Clear carriageway width must be at least 5.3 meters")
            
        # f value is constant 150 mm for all widths
        f = 0.15  # meters
        
        # Calculate g value based on carriageway width
        if 5.3 <= clear_carriageway_width <= 6.1:
            # Linear interpolation between 0.4m at 5.3m width and 1.2m at 6.1m width
            g = 0.4 + (clear_carriageway_width - 5.3) * (1.2 - 0.4) / (6.1 - 5.3)
        else:  # width > 6.1m
            g = 1.2  # meters
            
        clearance = {
            'g': round(g, 3),  # clearance in meters, rounded to 3 decimal places
            'f': f  # clearance in meters
        }
        return clearance

    @staticmethod
    def table_6(carriageway_width):
        """
        Determines the number of lanes for design purposes based on carriageway width
        as per IRC:6-2017 Table 6.
        
        Args:
            carriageway_width (float): The carriageway width (CW) in meters
            
        Returns:
            int: Number of lanes for design purposes
            
        Raises:
            ValueError: If the carriageway width is negative
        """
        if carriageway_width < 0:
            raise ValueError("Carriageway width cannot be negative")

        # Determine the number of lanes for design purposes based on ranges
        # Assign to variable `lanes` (so other functions can use it)
        if carriageway_width < 5.3:
            lanes = 1
        elif carriageway_width < 9.6:
            lanes = 2
        elif carriageway_width < 13.1:
            lanes = 3
        elif carriageway_width < 16.6:
            lanes = 4
        elif carriageway_width < 20.1:
            lanes = 5
        elif carriageway_width < 23.6:
            lanes = 6
        else:
            # For widths >= 23.6m, extrapolate using the same pattern
            # Each additional ~3.5 m adds one lane (approximate rule)
            additional_width = carriageway_width - 20.1
            additional_lanes = math.ceil(additional_width / 3.5)
            lanes = 6 + additional_lanes

        return lanes

    @staticmethod
    def table_6A(carriageway_width, design_lanes=None, g_increment=0.0, span=1.0, vehicle=None):
        """
        Computes the remaining carriageway width to be loaded as UDL and the
        resulting UDL (per metre length) based on Table 6A rules.

        Args:
            carriageway_width (float): carriageway width in meters
            design_lanes (int, optional): number of lanes for design purposes.
                If not provided, it will be determined by `table_6`.
            g_increment (float, optional): additional clearance increment
                (in metres) between adjacent vehicle lanes to be subtracted
                from the carriageway when computing remaining width. Default
                is 0.0 (no extra increment).

        Returns:
            dict: {
                'design_lanes': int,
                'vehicle_width': float,  # m (2.3 m)
                'f_m': float,            # clearance f in m
                'remaining_width': float,# width left for UDL (m, >=0)
                'udl_intensity_kg_m2': float, # 500 kg/m2 (by spec)
                'udl_kN_per_m': float    # UDL per metre length (kN/m)
            }

        Notes:
            - Uses `table_2` to obtain the f value (in mm) and converts to metres.
            - Vehicle width is taken as 2.3 m (1.8 + 0.5) as per the image.
            - Remaining width is computed as: CW - (lanes * vehicle_width) - 2*f
              where 2*f is clearance at both outer edges (minimum).
        """
        vehicle = ''
        # validate input
        if carriageway_width < 0:
            raise ValueError("Carriageway width cannot be negative")

        # determine design lanes if not provided
        if design_lanes is None:
            design_lanes = IRC6_2017.table_6(carriageway_width)

        # default vehicle for selection if not provided
        if vehicle is None:
            vehicle = KEY_VEHICLE[2] if len(KEY_VEHICLE) > 2 else ''

        # Branch by lane count
        if design_lanes == 1:
            # get f from table_3 (f returned in metres)
            f_info = IRC6_2017.table_3(carriageway_width)
            f_m = f_info.get('f', 0.15)

            vehicle_width = 2.3  # m (1.8 + 0.5)
            remaining_width = carriageway_width - (vehicle_width + 2.0 * f_m)

            # UDL intensity as specified for the remaining carriageway
            udl_intensity_kg_m2 = 500.0  # kg/m2
            udl_kg_per_m = udl_intensity_kg_m2 * max(remaining_width, 0.0) * span
            udl_kN_per_m = udl_kg_per_m * 9.81 / 1000.0

            return {
                'design_lanes': int(design_lanes),
                'vehicle_width': round(vehicle_width, 3),
                'f_m': round(f_m, 3),
                'remaining_width': round(remaining_width, 3),
                'udl_intensity_kg_m2': udl_intensity_kg_m2,
                'udl_kg_per_m': round(udl_kg_per_m, 3),
                'udl_kN_per_m': round(udl_kN_per_m, 3)
            }

        elif design_lanes == 2:
            # Class 70R (wheel vehicle)
            if vehicle == KEY_VEHICLE[0]:     # Class70R(W)
                f_m = 1.2  # metres
                vehicle_width = 2.790  # m
                remaining_width = carriageway_width - (vehicle_width + 2.0 * f_m)

                return {
                    'design_lanes': int(design_lanes),
                    'vehicle_width': round(vehicle_width, 3),
                    'f_m': round(f_m, 3),
                    'remaining_width': round(remaining_width, 3)
                }

            # Class A vehicles
            elif vehicle == KEY_VEHICLE[2]:   # ClassA
                f_info = IRC6_2017.table_3(carriageway_width)
                f_m = f_info.get('f', 0.15)
                g_m = f_info.get('g')

                vehicle_width = 2.3  # m (1.8 + 0.5)
                g_total = g_m + g_increment    #?
                remaining_width = carriageway_width - ((2.0 * vehicle_width) + g_total + (2.0 * f_m))

                return {
                    'design_lanes': int(design_lanes),
                    'vehicle_width': round(vehicle_width, 3),
                    'f_m': round(f_m, 3),
                    'remaining_width': round(remaining_width, 3)
                }

    

            # Class A vehicles
            elif vehicle == KEY_VEHICLE[2]:   # ClassA
                f_info = IRC6_2017.table_3(carriageway_width)
                f_m = f_info.get('f', 0.15)
                g_m = f_info.get('g')

                vehicle_width = 2.3  # m (1.8 + 0.5)
                g_total = g_m + g_increment    #?
                remaining_width = carriageway_width - ((2.0 * vehicle_width) + g_total + (2.0 * f_m))

                return {
                    'design_lanes': int(design_lanes),
                    'vehicle_width': round(vehicle_width, 3),
                    'f_m': round(f_m, 3),
                    'remaining_width': round(remaining_width, 3)
                }
        elif design_lanes == 3:
            if vehicle == KEY_VEHICLE[2]:   # ClassA
                f_info = IRC6_2017.table_3(carriageway_width)
                f_m = f_info.get('f', 0.15)
                g_m = f_info.get('g')

                vehicle_width = 2.3  # m (1.8 + 0.5)
                g_total = g_m + g_increment    #?
                remaining_width = carriageway_width - ((3.0 * vehicle_width) + (2.0 * f_m) + (2.0 * g_total))

                return {
                    'design_lanes': int(design_lanes),
                    'vehicle_width': round(vehicle_width, 3),
                    'f_m': round(f_m, 3),
                    'remaining_width': round(remaining_width, 3)
                }
            elif vehicle == KEY_VEHICLE[0] and KEY_VEHICLE[2]:  # Class70R(W) and ClassA
                f_info = IRC6_2017.table_3(carriageway_width)
                f_m = f_info.get('f', 0.15)
                g_m = f_info.get('g')
                vehicle_width_70R = 2.790  # m
                vehicle_width_A = 2.3  # m 
                vehicle_width = vehicle_width_70R + vehicle_width_A  # m
                g_total = 1.2 + g_increment
                remaining_width = carriageway_width - ((2.0 * vehicle_width) + (2.0 * f_m) + g_total)

                return {
                    'design_lanes': int(design_lanes),
                    'vehicle_width': round(vehicle_width, 3),
                    'f_m': round(f_m, 3),
                    'remaining_width': round(remaining_width, 3)
                }

    
    
    @staticmethod
    def table_7(span: float) -> float:
        """
        Returns the congestion factor for a given bridge span (in metres) as per Table 7 (image attached).

        Rules implemented:
        - For span <= 10 m: raises ValueError (table applies to spans above 10 m)
        - For 10 < span <= 30 m: congestion factor = 1.15 (constant)
        - For spans between the listed breakpoints (30,40,50,60,70) the congestion
          factor is linearly interpolated between the corresponding values.
        - For span >= 70 m: congestion factor = 1.70 (constant)

        Breakpoints used (span_m -> factor):
            30 -> 1.15
            40 -> 1.30
            50 -> 1.45
            60 -> 1.60
            70 -> 1.70

        Args:
            span (float): bridge span in metres

        Returns:
            float: congestion factor (rounded to 3 decimal places)
        """
        if span is None:
            raise ValueError("Span must be provided (in metres)")

        try:
            s = float(span)
        except Exception:
            raise ValueError("Span must be a number")

        if s <= 10.0:
            raise ValueError("Table 7 applies to spans above 10 m")

        # constant for upto 30 m
        if s <= 30.0:
            return round(1.15, 3)

        # constant for beyond 70 m
        if s >= 70.0:
            return round(1.70, 3)

        # Breakpoints for interpolation
        breakpoints = [
            (30.0, 1.15),
            (40.0, 1.30),
            (50.0, 1.45),
            (60.0, 1.60),
            (70.0, 1.70),
        ]

        # find interval that contains s
        for i in range(len(breakpoints) - 1):
            x0, y0 = breakpoints[i]
            x1, y1 = breakpoints[i + 1]
            if x0 <= s <= x1:
                # linear interpolation
                t = (s - x0) / (x1 - x0) if x1 != x0 else 0.0
                val = y0 + t * (y1 - y0)
                return round(val, 3)

        # fallback (should not reach here) - return nearest endpoint
        if s < breakpoints[0][0]:
            return round(breakpoints[0][1], 3)
        return round(breakpoints[-1][1], 3)
    
    @staticmethod
    def cl_204_6_fatigue_load():
        """
        Makes an Fatigue truck vehicle in local coordinates
        Returns a dictionary with keys:
            'x' - list of longitudinal load positions (m)
            'z' - list of transverse load positions (m)
            'wheel_loads' - list of wheel loads (kN)
        """
        # Define units
        axle_dist1= 4.50 * m
        axle_dist2= 1.40 * m
   

        # Define wheel loads (kN) for each longitudinal axle position
        # Mapping to the 3 longitudinal positions in `load_positions_x`.
        # Values provided by user (converted to kN):
        # [12, 14, 14]
        wheel_loads = [12 * kN, 14 * kN, 14 * kN]

        # Define longitudinal positions of each axle
        load_positions_x = [
                0,
                axle_dist1,
                axle_dist1 + axle_dist2,
                ]
            
        # Transverse position of each wheel
        load_positions_z = [-0.840, 0.840]

        # make a dictonary to return vehicle data
        return {
            'x': load_positions_x,
            'z': load_positions_z,
            'wheel_loads': wheel_loads
        }



