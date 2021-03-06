package mappings

import (
	grpcSpeech "github.com/GuyARoss/project-orva/pkg/grpc/speech"
	"github.com/GuyARoss/project-orva/pkg/orva"
)

// SpeechToResponse maps the speech response to the orva ctx response.
func SpeechToResponse(speech *grpcSpeech.SpeechResponse) *orva.Response {
	return &orva.Response{
		Statement:   speech.Message,
		GraphicURL:  speech.GraphicURL,
		GraphicType: speech.GraphicType,
		Duration:    speech.Duration,
	}
}
