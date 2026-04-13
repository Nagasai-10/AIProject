# Week 2 GPU and Session Risk Note

Week 2 planning identified operational risks affecting training reliability.

Key risks:
- Colab session timeout
- GPU interruption or instability
- incomplete artifact persistence
- inconsistent dependency behaviour

Mitigation direction:
- use Google Drive for persistence
- document dependencies clearly
- treat checkpoint saving as mandatory
- keep run history structured enough for later recovery and reporting

Purpose:
To improve reproducibility and reduce training evidence loss.
