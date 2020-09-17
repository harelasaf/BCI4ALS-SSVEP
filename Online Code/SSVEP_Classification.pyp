<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline computes the average power across channels in a moving window (for a specific frequency band), and then both plots it and sends it out over the network for pickup by another program (e.g., a game)." title="Simple Bandpower" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(100, 200)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="96e9e704-a908-4b27-96c4-1198e51297b4" version="1.0.0" />
		<node id="1" name="FIR Filter" position="(509.0, 60.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="b7c06d57-0298-4da5-bc7c-9e46630b0bd0" version="1.0.0" />
		<node id="2" name="Select Range" position="(200, 100)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range (channels)" uuid="06c249fb-c62f-4d9a-a039-1f5ed73607e5" version="1.0.0" />
		<node id="3" name="Time Series Plot" position="(1100, 200)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="5efb281e-acd2-4ecc-bc5c-33564b0fa8de" version="1.0.1" />
		<node id="4" name="LSL Output" position="(1313.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="a348cfac-6b7e-4560-b1cb-77a33572f598" version="1.0.0" />
		<node id="5" name="Stream Data" position="(190.0, 724.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="40f80a06-5183-4dfb-90d9-9a3cefaa9d24" version="1.1.0" />
		<node id="6" name="LSL Output" position="(290.0, 724.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="87798d67-d395-47a0-9df7-3fb76dbf7848" version="1.0.0" />
		<node id="7" name="Import XDF" position="(90.0, 724.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="f98e7015-9f1e-4c72-b348-623adfed5a10" version="1.0.0" />
		<node id="8" name="Inspect Data" position="(1100, 400)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data" uuid="bd2d6437-60c1-44b4-a955-37d425063c65" version="2.1.1" />
		<node id="9" name="Re-referencing" position="(400, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owrereferencing.OWRereferencing" title="Re-referencing" uuid="6b83c292-584a-4326-96ed-5995072f1753" version="1.0.0" />
		<node id="10" name="Select Range" position="(200, 300)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range (channels)" uuid="8fe1c5b1-5cd6-4c5a-842c-d1d899272f99" version="1.0.0" />
		<node id="11" name="Select Range" position="(855.0, 241.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range (channels)" uuid="e99053cf-f496-4066-adea-998a1ec38fb0" version="1.0.0" />
		<node id="12" name="FIR Filter" position="(510.0, 165.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="bbb548ab-0dae-47ae-a82b-170e4915c2e4" version="1.0.0" />
		<node id="13" name="FIR Filter" position="(513.0, 286.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="760ce43e-08da-4f6b-82fa-ed3630b34623" version="1.0.0" />
		<node id="14" name="FIR Filter" position="(515.0, 385.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="16d07271-81c6-4d9b-bd29-17d823cc1607" version="1.0.0" />
		<node id="15" name="Linear Discriminant Analysis" position="(660.0, 286.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="0af3af43-d37e-45d6-b3ad-3191e8505519" version="1.0.0" />
		<node id="16" name="Linear Discriminant Analysis" position="(660.0, 164.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="7e51f117-1ae2-4a3d-a60e-3d68cae62230" version="1.0.0" />
		<node id="17" name="Linear Discriminant Analysis" position="(662.0, 385.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="af457dd0-2bc8-4c8e-971a-bd4a34945db5" version="1.0.0" />
		<node id="18" name="Linear Discriminant Analysis" position="(660.0, 60.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="286627ed-cb22-4bad-9cb8-c2fe7b3c4883" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="5" sink_channel="Reference Data" sink_node_id="9" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="14" />
	</links>
	<annotations>
		<arrow end="(241.0, 314.0)" fill="#C1272D" id="0" start="(352.0, 378.0)" />
		<text font-family="Helvetica" font-size="16" id="1" rect="(314.0, 379.0, 82.0, 28.0)">ref channel</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
HlgMAAAAbWF4X2NodW5rbGVucQhLAFgMAAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVs
dClxClgFAAAAcXVlcnlxC1gUAAAAbmFtZT0nTXkgRGF0YXN0cmVhbSdxDFgHAAAAcmVjb3ZlcnEN
iFgUAAAAcmVzb2x2ZV9taW5pbXVtX3RpbWVxDkc/4AAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAAUHlRdDQuUXRDb3JlcRFYCgAAAFFCeXRl
QXJyYXlxEkMuAdnQywABAAAAAAAAAAACNAAAAXkAAAOyAAAACQAAAloAAAFwAAADqQAAAAAAAHET
hXEUh3EVUnEWWA4AAABzZXRfYnJlYWtwb2ludHEXiXUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsGSwdLB0sIZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMTfQBWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5
cQ1jc2lwCl91bnBpY2tsZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJh
eXEQQy4B2dDLAAEAAAAAAwwAAAFyAAAEhQAAAswAAAMVAAABmAAABHwAAALDAAAAAAAAcRGFcRKH
cRNScRRYDgAAAHNldF9icmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAADDAAAAasAAASFAAACkwAAAxUA
AAHRAAAEfAAAAooAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxYBQAAADA6IDIxcQ1Y
DgAAAHNldF9icmVha3BvaW50cQ6JWAQAAAB1bml0cQ9YBwAAAGluZGljZXNxEHUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKIWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDFgKAAAA
bGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/6AAAAAAAAFgMAAAA
bWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJvcRKJWA4AAABub19j
b25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBkZWZhdWx0KXEVWAwA
AABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReIWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVxGlgKAAAAUUJ5dGVB
cnJheXEbQy4B2dDLAAEAAAAAAwwAAADLAAAEgwAAA2oAAAMUAAAA6gAABHsAAANiAAAAAAAAcRyF
cR2HcR5ScR9YBQAAAHNjYWxlcSBHP+AAAAAAAABYDgAAAHNldF9icmVha3BvaW50cSGJWAwAAABz
aG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNYAAAAAHEkWAoAAAB0aW1lX3JhbmdlcSVH
QBQAAAAAAABYBQAAAHRpdGxlcSZYGAAAAEFscGhhIHBvd2VyIChtb3ZpbmcgYXZnKXEnWAoAAAB6
ZXJvX2NvbG9ycShYCQAAACM3RjdGN0Y3RnEpWAgAAAB6ZXJvbWVhbnEqiHUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAA8EAAAJFAAAFMAAA
A30AAAPFAAACXAAABSwAAAN5AAAAAQAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETWBAAAABteXVuaXF1ZWlkNDM1MzQ2
cRRYBQAAAHNyYXRlcRVYDQAAACh1c2UgZGVmYXVsdClxFlgLAAAAc3RyZWFtX25hbWVxF1gPAAAA
bXktcmVsYXhhdGlvbi0xcRhYCwAAAHN0cmVhbV90eXBlcRlYBwAAAENvbnRyb2xxGlgTAAAAdXNl
X2RhdGFfdGltZXN0YW1wc3EbiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEciXUu
</properties>
		<properties format="literal" node_id="5">{'hitch_probability': 15.0, 'jitter_percent': 5, 'looping': True, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAABAEAAAKxAAAFegAA
BC0AAAQKAAAC1wAABXEAAAQkAAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETWBIAAABteXVuaXF1ZWlkMDQ5ODUy
MDNxFFgFAAAAc3JhdGVxFVgNAAAAKHVzZSBkZWZhdWx0KXEWWAsAAABzdHJlYW1fbmFtZXEXWA0A
AABNeSBEYXRhc3RyZWFtcRhYCwAAAHN0cmVhbV90eXBlcRlYAwAAAEVFR3EaWBMAAAB1c2VfZGF0
YV90aW1lc3RhbXBzcRuIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0aW9ucRyJdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWBIAAABNdXNlRm9jdXNSZWxheC54ZGZxCFgTAAAAaGFuZGxlX2Nsb2NrX3Jl
c2V0c3EJiFgRAAAAaGFuZGxlX2Nsb2NrX3N5bmNxCohYFQAAAGhhbmRsZV9qaXR0ZXJfcmVtb3Zh
bHELiFgOAAAAbWF4X21hcmtlcl9sZW5xDFgNAAAAKHVzZSBkZWZhdWx0KXENWBIAAAByZW9yZGVy
X3RpbWVzdGFtcHNxDolYDgAAAHJldGFpbl9zdHJlYW1zcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXERY3NpcApfdW5waWNrbGVfdHlwZQpxElgMAAAAUHlRdDQu
UXRDb3JlcRNYCgAAAFFCeXRlQXJyYXlxFEMuAdnQywABAAD///0iAAAB1////pEAAAMj///9JgAA
Ae7///6NAAADHwAAAAAAAHEVhXEWh3EXUnEYWA4AAABzZXRfYnJlYWtwb2ludHEZiVgPAAAAdXNl
X3N0cmVhbW5hbWVzcRqJWAcAAAB2ZXJib3NlcRuJdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAoAAABhdXRvX2Nsb3NlcQKJWAgAAABjb2xfYXhp
c3EDWAUAAABzcGFjZXEEWAgAAABkZWNpbWFsc3EFSwhYDQAAAGV2ZXJ5X25fdGlja3NxBksKWA0A
AABmZXdlcl9idXR0b25zcQeIWAkAAABmb250X3NpemVxCEsKWBAAAABpbml0aWFsX3Bvc2l0aW9u
cQldcQooSxRLMk30AU2QAWVYCAAAAHJvd19heGlzcQtYBAAAAHRpbWVxDFgTAAAAc2F2ZWRXaWRn
ZXRHZW9tZXRyeXENY3NpcApfdW5waWNrbGVfdHlwZQpxDlgMAAAAUHlRdDQuUXRDb3JlcQ9YCgAA
AFFCeXRlQXJyYXlxEEMuAdnQywABAAAAAAMEAAABPQAABH0AAALPAAADDQAAAWMAAAR0AAACxgAA
AAAAAHERhXESh3ETUnEUWA4AAABzZXRfYnJlYWtwb2ludHEViVgPAAAAc2hvd19heGVzX3RhYmxl
cRaIWA8AAABzaG93X2RhdGFfdGFibGVxF4hYEgAAAHNob3dfbWFya2Vyc190YWJsZXEYiFgQAAAA
c2hvd19tYXhfY29sdW1uc3EZSwBYDwAAAHNob3dfbWF4X3ZhbHVlc3EaSzJYEgAAAHNob3dfc3Ry
ZWFtc190YWJsZXEbiFgLAAAAc3RyZWFtX25hbWVxHFgNAAAAKHVzZSBkZWZhdWx0KXEdWAwAAAB3
aW5kb3dfdGl0bGVxHlgTAAAASW5zcGVjdCBEYXRhIFBhY2tldHEfdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWAQAAABheGlzcQFYBQAAAHNwYWNlcQJYCAAAAGN1dF9wcm9wcQNHP7mZmZmZmZpYCQAA
AGVzdGltYXRvcnEEWAQAAABtZWFucQVYDwAAAHJlZmVyZW5jZV9yYW5nZXEGWAEAAAA6cQdYDgAA
AHJlZmVyZW5jZV91bml0cQhYBAAAAGF1dG9xCVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEKY3Np
cApfdW5waWNrbGVfdHlwZQpxC1gMAAAAUHlRdDQuUXRDb3JlcQxYCgAAAFFCeXRlQXJyYXlxDUMu
AdnQywABAAAAAAL2AAABaAAABIkAAAKAAAAC/wAAAY4AAASAAAACdwAAAAAAAHEOhXEPh3EQUnER
WA4AAABzZXRfYnJlYWtwb2ludHESiVgWAAAAdXNlX3NlcGFyYXRlX3JlZmVyZW5jZXETiXUu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDQu
UXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAAPAAAACAwAABTkAAALnAAADyQAA
AikAAAUwAAAC3gAAAAAAAHEIhXEJh3EKUnELWAkAAABzZWxlY3Rpb25xDF1xDShLFEsVZVgOAAAA
c2V0X2JyZWFrcG9pbnRxDolYBAAAAHVuaXRxD1gHAAAAaW5kaWNlc3EQdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYCQAAAGZyZXF1ZW5j
eXEDWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQRjc2lwCl91bnBpY2tsZV90eXBlCnEFWAwAAABQ
eVF0NC5RdENvcmVxBlgKAAAAUUJ5dGVBcnJheXEHQy4B2dDLAAEAAAAAAwMAAAGCAAAEfAAAAmYA
AAMMAAABqAAABHMAAAJdAAAAAAAAcQiFcQmHcQpScQtYCQAAAHNlbGVjdGlvbnEMWAEAAAA6cQ1Y
DgAAAHNldF9icmVha3BvaW50cQ6JWAQAAAB1bml0cQ9YBwAAAGluZGljZXNxEHUu
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsMSw1LDUsOZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMTfQBWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5
cQ1jc2lwCl91bnBpY2tsZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJh
eXEQQy4B2dDLAAEAAAAAAwMAAAGPAAAEfAAAAlkAAAMMAAABtQAABHMAAAJQAAAAAAAAcRGFcRKH
cRNScRRYDgAAAHNldF9icmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsOSw9LD0sQZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMTfQBWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5
cQ1jc2lwCl91bnBpY2tsZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJh
eXEQQy4B2dDLAAEAAAAAAwMAAAGPAAAEfAAAAlkAAAMMAAABtQAABHMAAAJQAAAAAAAAcRGFcRKH
cRNScRRYDgAAAHNldF9icmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsQSxFLEUsSZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMTfQBWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5
cQ1jc2lwCl91bnBpY2tsZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJh
eXEQQy4B2dDLAAEAAAAAAwMAAAGPAAAEfAAAAlkAAAMMAAABtQAABHMAAAJQAAAAAAAAcRGFcRKH
cRNScRRYDgAAAHNldF9icmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA0AAABjbGFzc193ZWlnaHRzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgKAAAAY29uZF9m
aWVsZHEDWAsAAABUYXJnZXRWYWx1ZXEEWBAAAABkb250X3Jlc2V0X21vZGVscQWJWA8AAABpbml0
aWFsaXplX29uY2VxBohYCQAAAG51bV9mb2xkc3EHSwVYDQAAAHByb2JhYmlsaXN0aWNxCIhYEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUKcQpYDAAAAFB5UXQ0LlF0
Q29yZXELWAoAAABRQnl0ZUFycmF5cQxDLgHZ0MsAAQAAAAADAwAAAZwAAAR8AAACTAAAAwwAAAHC
AAAEcwAAAkMAAAAAAABxDYVxDodxD1JxEFgNAAAAc2VhcmNoX21ldHJpY3ERWAgAAABhY2N1cmFj
eXESWA4AAABzZXRfYnJlYWtwb2ludHETiVgJAAAAc2hyaW5rYWdlcRRYBAAAAGF1dG9xFVgGAAAA
c29sdmVycRZYBQAAAGVpZ2VucRdYCQAAAHRvbGVyYW5jZXEYRz8aNuLrHEMtWAkAAAB2ZXJib3Np
dHlxGUsAdS4=
</properties>
		<properties format="literal" node_id="16">{'class_weights': '(use default)', 'cond_field': 'TargetValue', 'dont_reset_model': False, 'initialize_once': True, 'num_folds': 5, 'probabilistic': True, 'savedWidgetGeometry': None, 'search_metric': 'accuracy', 'set_breakpoint': False, 'shrinkage': 'auto', 'solver': 'eigen', 'tolerance': 0.0001, 'verbosity': 0}</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA0AAABjbGFzc193ZWlnaHRzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgKAAAAY29uZF9m
aWVsZHEDWAsAAABUYXJnZXRWYWx1ZXEEWBAAAABkb250X3Jlc2V0X21vZGVscQWJWA8AAABpbml0
aWFsaXplX29uY2VxBohYCQAAAG51bV9mb2xkc3EHSwVYDQAAAHByb2JhYmlsaXN0aWNxCIhYEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUKcQpYDAAAAFB5UXQ0LlF0
Q29yZXELWAoAAABRQnl0ZUFycmF5cQxDLgHZ0MsAAQAAAAADAwAAAZwAAAR8AAACTAAAAwwAAAHC
AAAEcwAAAkMAAAAAAABxDYVxDodxD1JxEFgNAAAAc2VhcmNoX21ldHJpY3ERWAgAAABhY2N1cmFj
eXESWA4AAABzZXRfYnJlYWtwb2ludHETiVgJAAAAc2hyaW5rYWdlcRRYBAAAAGF1dG9xFVgGAAAA
c29sdmVycRZYBQAAAGVpZ2VucRdYCQAAAHRvbGVyYW5jZXEYRz8aNuLrHEMtWAkAAAB2ZXJib3Np
dHlxGUsAdS4=
</properties>
		<properties format="literal" node_id="18">{'class_weights': '(use default)', 'cond_field': 'TargetValue', 'dont_reset_model': False, 'initialize_once': True, 'num_folds': 5, 'probabilistic': True, 'savedWidgetGeometry': None, 'search_metric': 'accuracy', 'set_breakpoint': False, 'shrinkage': 'auto', 'solver': 'eigen', 'tolerance': 0.0001, 'verbosity': 0}</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node1",
            "data",
            "node3",
            "data"
        ],
        [
            "node1",
            "data",
            "node11",
            "data"
        ],
        [
            "node6",
            "data",
            "node7",
            "data"
        ],
        [
            "node8",
            "data",
            "node6",
            "data"
        ],
        [
            "node3",
            "data",
            "node10",
            "data"
        ],
        [
            "node11",
            "data",
            "node10",
            "reference_data"
        ],
        [
            "node10",
            "data",
            "node2",
            "data"
        ],
        [
            "node10",
            "data",
            "node13",
            "data"
        ],
        [
            "node10",
            "data",
            "node14",
            "data"
        ],
        [
            "node10",
            "data",
            "node15",
            "data"
        ],
        [
            "node14",
            "data",
            "node16",
            "data"
        ],
        [
            "node2",
            "data",
            "node19",
            "data"
        ],
        [
            "node13",
            "data",
            "node17",
            "data"
        ],
        [
            "node15",
            "data",
            "node18",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='My Datastream'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "96e9e704-a908-4b27-96c4-1198e51297b4"
        },
        "node10": {
            "class": "Rereferencing",
            "module": "neuropype.nodes.signal_processing.Rereferencing",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "cut_prop": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "estimator": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "mean"
                },
                "reference_range": {
                    "customized": false,
                    "type": "Port",
                    "value": ":"
                },
                "reference_unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_separate_reference": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "6b83c292-584a-4326-96ed-5995072f1753"
        },
        "node11": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        20,
                        21
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "8fe1c5b1-5cd6-4c5a-842c-d1d899272f99"
        },
        "node12": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "frequency"
                },
                "selection": {
                    "customized": false,
                    "type": "Port",
                    "value": ":"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "e99053cf-f496-4066-adea-998a1ec38fb0"
        },
        "node13": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        12,
                        13,
                        13,
                        14
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "bbb548ab-0dae-47ae-a82b-170e4915c2e4"
        },
        "node14": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        14,
                        15,
                        15,
                        16
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "760ce43e-08da-4f6b-82fa-ed3630b34623"
        },
        "node15": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        16,
                        17,
                        17,
                        18
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "16d07271-81c6-4d9b-bd29-17d823cc1607"
        },
        "node16": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "Port",
                    "value": "auto"
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "eigen"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "0af3af43-d37e-45d6-b3ad-3191e8505519"
        },
        "node17": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "Port",
                    "value": "auto"
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "eigen"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "7e51f117-1ae2-4a3d-a60e-3d68cae62230"
        },
        "node18": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "Port",
                    "value": "auto"
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "eigen"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "af457dd0-2bc8-4c8e-971a-bd4a34945db5"
        },
        "node19": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "Port",
                    "value": "auto"
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "eigen"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "286627ed-cb22-4bad-9cb8-c2fe7b3c4883"
        },
        "node2": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        6,
                        7,
                        7,
                        8
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "b7c06d57-0298-4da5-bc7c-9e46630b0bd0"
        },
        "node3": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": "0: 21"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "06c249fb-c62f-4d9a-a039-1f5ed73607e5"
        },
        "node4": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": ""
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Alpha power (moving avg)"
                },
                "zero_color": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "5efb281e-acd2-4ecc-bc5c-33564b0fa8de"
        },
        "node5": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "myuniqueid435346"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "my-relaxation-1"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a348cfac-6b7e-4560-b1cb-77a33572f598"
        },
        "node6": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "hitch_probability": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 15.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "40f80a06-5183-4dfb-90d9-9a3cefaa9d24"
        },
        "node7": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "myuniqueid04985203"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "My Datastream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "87798d67-d395-47a0-9df7-3fb76dbf7848"
        },
        "node8": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MuseFocusRelax.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f98e7015-9f1e-4c72-b348-623adfed5a10"
        },
        "node9": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "auto_close": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "col_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "decimals": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 8
                },
                "every_n_ticks": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 10
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "row_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_max_columns": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 0
                },
                "show_max_values": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 50
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "bd2d6437-60c1-44b4-a955-37d425063c65"
        }
    },
    "version": 1.1
}</patch>
</scheme>
