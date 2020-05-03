# Lighthouse v2 DIY tracker

A bunch of gathered information about the HTC Vive tracking system used with the Base Stations v2 (one rotor).

## Definitions

- **Base station** or **lighthouse**: a HTC Vive base station v2

## Base stations parameters

- Beam data
  - Modulation frequency: 6 MHz
  - Encoding method: BMC
  - Frame length: 17 bits
  - Content: maximum length 17-bits LFSR
- Sweep
  - Frequency: ~50 Hz

## Sensors

Each sensor captures:

- Arrival timestamp `time`
- Cipher `cipher`, the first 17 bits of encoded data in the beam carrier
- LFSR polynomial used to generate the beam data
- Time offset `offset`, from basestation sync event and the received pulse
- Sensor ID (each sensor has its own ID)
- Width of the received pulse `width`

Width can be used to approximate the distance from the basestation.


```
   <---> 166 ns (6 MHz)

   +---+ +-+   +-+ +-+ +---+
   |   | | |   | | | | |   |               Encoded data
---+   +-+ +---+ +-+ +-+   +--- ...
    1 1 0 1 0 0 1 0 1 0 1 1 0 0            BMC data
    --- --- --- --- --- --- ---
     0   1   0   1   1   0   0             Cipher
---+                                  +---
   |                                  |    Envelope
   +--------------------------- ... --+
   <---------------------------------->
                  width

   ^ Arrival Time
```

## Polynomials

32 polynomials appear to be used on a v2 lighthouse.

Channel of the base station is `(nPoly / 2 + 1)`
Each base station uses 2 polynomials to encode one bit of **slow data**

Slow bit is `nPoly & 0x01`


# Signal

Signal is at 6MHz once demodulated. An entire period takes 21.85 ms (`(2**17-1) / 6e6`).

# OOTX

OOTX stands for Omnidirectional Optical Transmitter. Each base station has its own set of eccentricities or non-ideal behavior. At the factory, these non-ideal parameters are calculated and stored in the base station. In the field, each base station transmits its calibration parameters.

Within v1, the OOTX data were sent through the sync pulses. In v2, they are encoded in the beam at one bit per sweep.

Slow data ? It gives sensor device information on the lighthouse:

- Serial number
- Calibration data
- ...

# Modes?

16 modes ofr the LH2 each has a slighly different rotation frequency and two distinct polynomials used. OOTX is about 128 bytes (bitrate about 100 bps

# Multiple Lighthouses?

No synchronization between lighouses ? This explains why each lighthouse has different RPM. Collisions would be very rare.

## Correlation between two sensors

Find sync time by runniong LFSR from 1 until reach value

## RPM modes

- 21.85 ms
- 19.98 ms

## Architecture

A possible architecture overview

![architecture](assets/diagram.svg)


## References and Resources

- [ESPTracker issue #1](https://github.com/cnlohr/esptracker/issues/1)
- [Lighthouse v2 pictures](https://drive.google.com/drive/folders/1cRZ3P2-qimd7ccLXDEDPEvQxj6XS1rv1)
- [libdeepdive](https://github.com/asymingt/deepdive)
- [Tundra Labs TL448K6D](https://static1.squarespace.com/static/5c23a4e41137a63d93190b61/t/5e1e074936fe03405bf50116/1579026250766/TL448K6D-VR_Datasheet_v1p1.pdf)
- [LFSR Polynomials](https://github.com/cntools/libsurvive/blob/c1ca3657fd305a5aef60ac862c9ff60aa67469c9/src/lfsr_lh2.c#L22)
- [Lighthouse2Tools](https://github.com/jdavidberger/lighthouse2tools)
- [Discord](https://discord.gg/WYYJyc2)
- [libsurvive](https://github.com/cntools/libsurvive)
- [Alan Yates conference](https://hackaday.com/2016/12/21/alan-yates-why-valves-lighthouse-cant-work/)
- [Crazyflie LH2 prototype](https://github.com/ataffanel/crazyflie-lh2-prototype)
- [Manchester-BMC on EFM8LB1](https://github.com/MarkDing/Manchester-BMC)
- [Silabs AN921 BMC Decoder](https://www.silabs.com/documents/public/application-notes/AN921.pdf)
- [Lighthouse deck schematic](https://wiki.bitcraze.io/_media/projects:crazyflie2:expansionboards:lighthouse_deck-revd-schematic.pdf)
- [Bitcraze Lighthouse positionning deck](https://store.bitcraze.io/products/lighthouse-positioning-deck)
- [OOTX data](http://help.triadsemi.com/en/articles/882180-ootx-lighthouse-base-station-data)
- [LKighthouseRedox](https://github.com/nairol/LighthouseRedox)
