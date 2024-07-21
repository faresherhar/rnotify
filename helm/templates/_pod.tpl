{{- define "rnotify.pod" -}}
{{- with .Values.imagePullSecrets }}
imagePullSecrets:
{{- toYaml . | nindent 2 }}
{{- end }}
{{- with .Values.extraInitContainers }}
initContainers:
  {{- toYaml . | nindent 2 }}
{{- end }}
containers:
  {{- with .Values.extraContainers }}
    {{- toYaml . | nindent 2 }}
  {{- end }}
  - name: {{ .Values.rnotify.name }}
    image: {{ .Values.rnotify.image.registry }}/{{ .Values.rnotify.image.repository }}:{{ .Values.rnotify.image.tag }}
    {{- with .Values.rnotify.command }}
    command:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    {{- with .Values.rnotify.resources }}
    resources:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    volumeMounts:
      - name: tmp
        mountPath: /tmp
      - name: config
        mountPath: /etc/rnotify/config.toml
        subPath: config.toml
    {{- with .Values.rnotify.extraVolumeMounts }}
      {{- toYaml . | nindent 6 }}
    {{- end }}
    imagePullPolicy: {{ .Values.rnotify.imagePullPolicy }}
    {{- with .Values.rnotify.podSecurityContext }}
    securityContext:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    env:
      - name: RNOTIFY_CONFIG_FILE
        value: /etc/rnotify/config.toml
    {{- with .Values.rnotify.env }}
      {{- toYaml . | nindent 6 }}
    {{- end }}
restartPolicy: OnFailure
{{- with .Values.rnotify.securityContext }}
securityContext:
	{{- toYaml . | nindent 2 }}
{{- end }}
{{- with .Values.rnotify.nodeSelector }}
nodeSelector:
  {{- toYaml . | nindent 2 }}
{{- end }}
{{- with .Values.rnotify.affinity }}
affinity:
  {{- toYaml . | nindent 2 }}
{{- end }}
{{- with .Values.rnotify.tolerations }}
tolerations:
  {{- toYaml . | nindent 2 }}
{{- end }}
volumes:
  - name: tmp
    emptyDir: {}
  - name: config
    configMap:
      name: {{ include "rnotify.fullname" . }}-config
{{- with .Values.rnotify.extraVolumes }}
  {{- toYaml . | nindent 2 }}
{{- end }}
{{- end }}