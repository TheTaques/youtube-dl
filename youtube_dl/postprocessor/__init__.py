from __future__ import unicode_literals

from .embedthumbnail import EmbedThumbnailPP
from .ffmpeg import (
    FFmpegPostProcessor,
    FFmpegEmbedSubtitlePP,
    FFmpegExtractAudioPP,
    FFmpegFixupStretchedPP,
    FFmpegFixupM3u8PP,
    FFmpegFixupM4aPP,
    FFmpegMergerPP,
    FFmpegMetadataPP,
    FFmpegVideoConvertorPP,
    FFmpegSubtitlesConvertorPP,
    FFmpegMergerAndMetadataPP,
)
from .xattrpp import XAttrMetadataPP
from .execafterdownload import ExecAfterDownloadPP
from .metadatafromtitle import MetadataFromTitlePP


def get_postprocessor(key):
    return globals()[key + 'PP']


__all__ = [
    'EmbedThumbnailPP',
    'ExecAfterDownloadPP',
    'FFmpegEmbedSubtitlePP',
    'FFmpegExtractAudioPP',
    'FFmpegFixupM3u8PP',
    'FFmpegFixupM4aPP',
    'FFmpegFixupStretchedPP',
    'FFmpegMergerPP',
    'FFmpegMetadataPP',
    'FFmpegPostProcessor',
    'FFmpegSubtitlesConvertorPP',
    'FFmpegVideoConvertorPP',
    'MetadataFromTitlePP',
    'XAttrMetadataPP',
    'FFmpegMergerAndMetadataPP'
]
