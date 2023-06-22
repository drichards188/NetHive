cd databus
python receive_logs_topic.py "kern.*" "alpha" &
python receive_logs_topic.py "kern.*" "beta" &
python emit_log_topic.py "kern.critical" "A critical kernel error" &
python emit_log_topic.py "kern.route" "go to beta" &

